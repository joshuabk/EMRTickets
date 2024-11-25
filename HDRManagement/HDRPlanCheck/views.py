from django.shortcuts import render, redirect

from Patient.models import Patient

import pydicom as pyd

import datetime



from. import HDRFunctions as df
from. import HDRDoseCalc as dc
from. import HDRPlanChecks as pc

from .forms import  editCylinderCheckActivations,  editCylinderCheckValues, editTOCheckActivations, editTOCheckValues
from .models import HDRPlan, HDRCourse, Channel, SourceControlPoint, DosePoint, tempPlanFile, HDRFraction, HDRPlanCheckSet, HDRPlanCheck, CylinderCheckActivation, CheckSetValuesCylinder, TOCheckActivation, CheckSetValuesTO 

# Create your views here

def Home(request):
    return render(request, 'Home.html', {})


def importPlan(request):
    return render(request, 'ImportPlan.html', {})

def importPlanFileToCourse(request):
    return render(request, 'ImportPlanFileToCourse.html', {})


def showImportedPlan(request):

    print(request.method)
    if request.method  == 'POST':
        #form = SaveFileForm(request.POST, request.FILES)
        File = request.FILES['dicomFile']
        #print(form.errors)
        planFile = File
        currentDateTime = datetime.datetime.now()
        dataPlan = pyd.dcmread(planFile)
        patient = df.getPatientAndSave(dataPlan)
        
        course = df.getCourseAndSave(dataPlan, patient)
        plan = df.getPlanAndSave(dataPlan, course)
        currentActivity = df.calcNewActivity(plan.RefDate,  currentDateTime, plan.Kerma)
        currentTxTime = df.calcCurrentTxTime(plan.PlanActivity, currentActivity, plan.Time)
        channelSet, controlPSet = df.getChannelsAndControlPointsAndSave(dataPlan, plan)
        dosePointSet = df.getDosePointsandSave(dataPlan, plan)
        print("Post")
        
         
        return render(request, 'ShowHDRPlan.html', {'Patient': patient, 'HDRCourse':course, 'HDRPlan':plan, 'ChannelSet':channelSet, 'ControlPointSet': controlPSet, 'CurrentActivity': currentActivity,'CurrentTxTime': currentTxTime, 'CurrentDateTime': currentDateTime, 'DosePointSet': dosePointSet})
    else:
         print("Not Post")
         return render(request, 'ImportPlan.html', {})

def openHDRCourse(request):
    #HDRCourse.objects.all().delete()
    patientSet = Patient.objects.all()
    courseSet = HDRCourse.objects.all()
    
    return render(request, 'OpenHDRCourse.html', {'patients': patientSet,'courses':courseSet})


def openHDRPlan(request, course_id):

    #patientSet = Patient.objects.filter()
    course = HDRCourse.objects.get(pk = course_id)
    print(course.pk)
    planSet = HDRPlan.objects.all()
     
    return render(request, 'OpenHDRPlan.html', {'course':course, 'planSet': planSet})

def deletePatient(request, patient_id):

    #patientSet = Patient.objects.filter()
    print(patient_id)
    delPatient = Patient.objects.get(pk =  patient_id)#.delete()
    delPatient.delete()

    return redirect('openHDRCourse')

def deleteHDRCourse(request, course_id):

    patientSet = Patient.objects.filter()
    print(course_id)
    delCourse = HDRCourse.objects.get(pk =  course_id)#.delete()
    delCourse.delete()

    return redirect('openHDRCourse')



def showHDRPlan(request, plan_id):

    #patientSet = Patient.objects.filter()
    currentDateTime = datetime.datetime.now() 
    plan = HDRPlan.objects.get(pk = plan_id)
    course = plan.Course
    channels = Channel.objects.filter(Plan = plan)
    controlPointSet  = SourceControlPoint.objects.all()

    currentActivity = df.calcNewActivity(plan.RefDate,  currentDateTime, plan.Kerma)
    currentTxTime = df.calcCurrentTxTime(plan.PlanActivity, currentActivity, plan.Time)

    fractions = HDRFraction.objects.filter(HDRCourse = course)
    
    return render(request, 'ShowHDRPlan.html', {'HDRPlan':plan, 'CurrentActivity':currentActivity, 'CurrentTxTime':currentTxTime, 'ChannelSet':channels, 'ControlPointSet':controlPointSet, 'CurrentDateTime': currentDateTime, 'Fractions': fractions })

def calcDose(request, plan_id):
    CPs = []
    DoseList =[]
    planDoseList = []

    plan = HDRPlan.objects.get(pk = plan_id)
    channels  = list(Channel.objects.filter(Plan = plan))
    for channel in channels:
        CPs = CPs + list(SourceControlPoint.objects.filter(Channel = channel))
    DPs = list(DosePoint.objects.filter(HDRPlan = plan))
    for DP in DPs:
        calcDose = dc.calcTotalDoseForDP(CPs, DP, plan)
        error = dc.calcDoseError(float(DP.Dose), calcDose)
        DoseList.append({'Calced Dose': round(calcDose,4), 'Plan Dose':float(DP.Dose), 'Error': error})
        
    #print(calcDose)
    return render(request, 'showDose.html', {'DoseList':DoseList }) 


def createCourse(request):
    return render(request, 'CreateCourse.html', {}) 

def saveCourse(request):
    
    if request.method  == 'POST':  
            #print(form.errors)
            files = tempPlanFile.objects.all()
            FileModel = files[0]
            currentDateTime = datetime.datetime.now()
            dataPlan = pyd.dcmread(FileModel.TempFile)

            patientID = df.getPtID(dataPlan)
            patients  = list(Patient.objects.filter(PatientID = patientID))
           
            print(len(patients))
            if len(patients) < 1:
                
                patient = df.getPatientAndSave(dataPlan)
            else:
                print("Patient ID")
                print(patients[0].PatientID)
                patient = patients[0]
            courseName = request.POST['CourseName']
            courseType = request.POST['CourseType']
            treatmentType = request.POST['TxType']
            numFx = request.POST['NumFractions']
            rxDose = request.POST['RXDose']
            rxDist = request.POST['RXDist']

            course = df.getCourseAndSave(dataPlan, patient, courseName, courseType, rxDose, rxDist, numFx, treatmentType)
            #course = df.getCourseAndSave(dataPlan, patient, courseName, courseType, rxDose, numFx)
            #course1 = course
            plan = df.getPlanAndSave(dataPlan, course)
            currentActivity = df.calcNewActivity(plan.RefDate,  currentDateTime, plan.Kerma)
            currentTxTime = df.calcCurrentTxTime(plan.PlanActivity, currentActivity, plan.Time)
            channelSet, controlPSet = df.getChannelsAndControlPointsAndSave(dataPlan, plan)
            dosePointSet = df.getDosePointsandSave(dataPlan, plan)
            df.createSinglePlanFractions(course, numFx, plan, rxDose, course.TxType)

            fractions = HDRFraction.objects.filter(HDRCourse = course)

            

            return render(request, 'ShowHDRPlan.html', {'HDRPlan':plan, 'CurrentActivity':currentActivity, 'CurrentTxTime':currentTxTime, 'ChannelSet': channelSet, 'ControlPointSet':controlPSet, 'CurrentDateTime': currentDateTime, 'Fractions': fractions}) 
            

def importPlanToCourse(request):
    print(request.FILES['planFile'])
    if request.method  == 'POST':
        #form = SaveFileForm(request.POST, request.FILES)
        tempPlanFile.objects.all().delete()
        File = request.FILES['planFile']
        #print(form.errors)
        planFile = File
        currentDateTime = datetime.datetime.now()
        dataPlan = pyd.dcmread(planFile)

        tempFile = tempPlanFile.create(planFile)
        tempFile.save()
        
        Activity =  df.getRefActivity(dataPlan)

        patientName = df.getPtName(dataPlan)

        return render(request, 'CreateCourse.html', {'PatientName':patientName, 'PlanFile': planFile })
    else:
         print("Not Post")
         return render(request, 'CreateCourse.html',{})

def checkCylinderPlan(request, plan_id):
    plan = HDRPlan.objects.filter(pk = plan_id).first()
    planCheckSet = HDRPlanCheckSet.objects.filter(Plan = plan).first()
    course = plan.Course
    HDRPlanCheck.objects.filter(PlanCheckSet = planCheckSet)
    RXDist = plan.Course.RXDist
    checks = []
    if course.TxType == "Cylinder":
        RXDist = plan.Course.RXDist
        HDRPlanCheck.objects.filter(PlanCheckSet = planCheckSet).delete()
        pc.createCylinderCheckSet(plan, planCheckSet, RXDist)

        checks = list(HDRPlanCheck.objects.filter(PlanCheckSet = planCheckSet))

    if course.TxType == "T&O":

        
        HDRPlanCheck.objects.filter(PlanCheckSet = planCheckSet).delete()

        pc.createTOCheckSet(plan, planCheckSet)
        checks = list(HDRPlanCheck.objects.filter(PlanCheckSet = planCheckSet))

    return render(request, 'ShowPlanChecks.html', {'Checks':checks, 'Plan': plan, 'Course':course })   
        
def selectPlanChecksCylinder(request):
     actList =  CylinderCheckActivation.objects.all().first()
     valueList = CheckSetValuesCylinder.objects.all().first()
     editFormCyl =  editCylinderCheckActivations(instance =  actList)
     valueFormCyl = editCylinderCheckValues(instance =  valueList)
     return render(request, 'selectCheckTemps/SelectChecksCylinder.html', {'CheckList':actList, 'editFormCyl': editFormCyl, 'valueFormCyl': valueFormCyl })

def selectPlanChecksTO(request):
     actList =  TOCheckActivation.objects.all().first()
     valueList = CheckSetValuesTO.objects.all().first()
     editFormTO =  editTOCheckActivations(instance =  actList)
     valueFormTO = editTOCheckValues(instance =  valueList)
     return render(request, 'selectCheckTemps/SelectChecksTO.html', {'CheckList':actList, 'editFormTO': editFormTO, 'valueFormTO': valueFormTO }) 


def saveSelectedPlanChecksTO(request):
    if request.method == "POST": 
        print(request.POST)
        editFormTO = editTOCheckActivations(request.POST or None)
        valueFormTO = editTOCheckValues(request.POST or None)
        
        if editFormTO.is_valid():
            TOCheckActivation.objects.all().delete()
            editFormTO.save()
            print("Edit Form is good")
        else:
            print("Edit Form is bad")
        if valueFormTO.is_valid():
            CheckSetValuesTO.objects.all().delete()
            valueFormTO.save()
        else:
            print("Value Form is bad")

    actListTO =  TOCheckActivation.objects.all().first()
    valueListTO = CheckSetValuesTO.objects.all().first()
    valueFormTO =  editTOCheckValues(instance =  valueListTO)
    editFormTO = editTOCheckActivations(instance = actListTO)
    return render(request, 'selectCheckTemps/SelectChecksTO.html', {'CheckList':actListTO, 'editFormTO': editFormTO, 'valueFormTO': valueFormTO})


def saveSelectedPlanChecksCylinder(request):
    if request.method == "POST": 
        editFormCyl = editCylinderCheckActivations(request.POST or None)
        valueFormCyl = editCylinderCheckValues(request.POST or None)
         
        if editFormCyl.is_valid():
            CylinderCheckActivation.objects.all().delete()
            editFormCyl.save()
        if valueFormCyl.is_valid():
            CheckSetValuesCylinder.objects.all().delete()
            valueFormCyl.save()

    actList =  CylinderCheckActivation.objects.all().first()
    valueList = CheckSetValuesCylinder.objects.all().first()
    valueFormCyl =  editCylinderCheckValues(instance =  valueList)
    editFormCyl = editCylinderCheckActivations(instance = actList)
    return render(request, 'selectCheckTemps/SelectChecksCylinder.html', {'CheckList':actList, 'editFormCyl': editFormCyl, 'valueFormCyl': valueFormCyl})

        
           
            
 


    