import datetime
import math
from .models import HDRPlan, HDRCourse, dicomFiles,  SourceControlPoint, Channel, DosePoint, HDRFraction, HDRPlanCheckSet, HDRTxCheckSet

from Patient.models import Patient


def getPtName(plan):
  
   PtName = str(plan.PatientName)
   PtName = PtName[:-3]
   PtName = PtName.replace('^',', ')
   return PtName

def getPtID(plan):
  
   ptID = plan.PatientID
   return ptID
def getPtDOB(plan):
  
   ptDOB = plan.PatientBirthDate
   newDate = formateDate(ptDOB)
   return newDate

def formateDate(DicomDate):
    print(DicomDate)
    if(DicomDate):
        DjangoDate = datetime.date(int(DicomDate[0:4]), int(DicomDate[4:6]), int(DicomDate[6:8]))
        return DjangoDate
    else:
        return None



def getCourseName(plan):
    Cname = plan.StudyDescription
    return Cname

name = 'josh'
def getPlanName(plan):
    planName = plan.RTPlanName
    planName = planName.replace(' ','')
    planName = planName.replace('.','_')
    return planName

def getAirKerma(plan):
    airKerma = plan.SourceSequence[0].ReferenceAirKermaRate
    return round(float(airKerma),3)

def getRefActivity(plan):
    airKerma = plan.SourceSequence[0].ReferenceAirKermaRate
    refActivity = airKerma * 0.00024497
    return round(float(refActivity),3)

def getReferenceDate(plan):
    refDate = plan.SourceSequence[0].SourceStrengthReferenceDate
    refTime = plan.SourceSequence[0].SourceStrengthReferenceTime
    date = datetime.datetime(int(refDate[0:4]), int(refDate[4:6]), int(refDate[6:8]), int(refTime[0:2]), int(refTime[2:4]), int(refTime[4:6]))
    return date

def getChannelMapNumber(plan):
    chanMapNumber = plan.ApplicationSetupSequence[0].ChannelSequence[0].TransferTubeNumber
    return chanMapNumber

def getChannelIDNumber(plan):
    chanIDNumber = plan.ApplicationSetupSequence[0].ChannelSequence[0].TransferTubeNumber
    return chanIDNumber

def getChannelLength(plan):
    chanLength = plan.ApplicationSetupSequence[0].ChannelSequence[0].ChannelLength
    return chanLength

def getStepSize(plan):
    chanStepSize = plan.ApplicationSetupSequence[0].ChannelSequence[0].SourceApplicatorStepSize
    return chanStepSize

def getChannelSourcePosittions(plan):
    sourcePosSequence = plan.ApplicationSetupSequence[0].ChannelSequence[0].BrachyControlPointSequence
    SourcePositions = []
    for pos in sourcePosSequence:
        SourcePositions.append(pos.ContorlPoint3DPosition)

#def calcDistanceToNearestSourcePos(SourcePositions, PointPos):


def calcNewActivity(calDate, currDate, refAirKerma):
    dateDiff = currDate - calDate
    currAirKerma = float(refAirKerma) * math.exp(-0.00000010866 * dateDiff.total_seconds())
    currActivity = currAirKerma * 0.00024497
    currActivity = round(currActivity, 3)
    return currActivity

def getTotalTxTime(plan):
    totalTime = 0
    for chan in plan.ApplicationSetupSequence[0].ChannelSequence:
        chan.ChannelTotalTime
        totalTime = totalTime + chan.ChannelTotalTime
        return totalTime
    
def getRxDose(plan):
   dose = plan.FractionGroupSequence[0].ReferencedBrachyApplicationSetupSequence[0].BrachyApplicationSetupDose
   dose = float(dose) * 100
   return dose

def getNumberFx(plan):
    numFx = plan.FractionGroupSequence[0].NumberOfFractionsPlanned
    return numFx

def getNumOfChannels(plan):
    numChan = plan.FractionGroupSequence[0].NumberOfBrachyApplicationSetups
    return numChan

def getAfterLoaderName(plan):
    MachineName = plan.TreatmentMachineSequence[0].TreatmentMachineName
    
    return MachineName

def getIsotopeName(plan):
    IsotopeName = plan.TreatmentMachineSequence[0].TreatmentMachineName
    
    return IsotopeName

def calcCurrentTxTime(refActivity, curActivity, refTime):
    curTime = (float(refActivity)/curActivity)  * float(refTime)
    
    return round(curTime, 2)


    # def create(cls, planName, channelIDNumber, channelMapNumber, numberOFControlPoints, stepSize, channelLength, channelTime, finalTimeWeight)
    #    channel =  cls(PlanName =  planName, ChannelIDNumber = channelIDNumber, ChannelMapNumber= channelMapNumber, StepSize = stepSize, ChannelLength = channelLength, ChannelTime = channelTime, FinalTimeWeight = finalTimeWeight)
    #    return channel
def getPatientAndSave(plan):
    PtName = str(getPtName(plan))
    
    PtID = getPtID(plan)
    PtDOB = getPtDOB(plan)
    patient = Patient.create(PtName,  PtDOB, PtID)
    patient.save()
    return patient
    
def getCourseAndSave(plan, patient, courseName, courseType, rxDose, rxDist,  numFractions, txType):
    patientName = str(getPtName(plan))
    print(patientName)
  
    print(patient)

    course = HDRCourse.create(courseName, patient, patientName, courseType, rxDose, rxDist,  numFractions, txType)
    course.save()
    return course

def createPlanCheckSet(plan, checkType):
    planCheckSet = HDRPlanCheckSet.create(plan, checkType)
    planCheckSet.save()
    return planCheckSet

def createTxCheckSet(fraction, checkType):
    TxCheckSet = HDRTxCheckSet.create(fraction, checkType)
    TxCheckSet.save()
    return TxCheckSet


def createMultiPlanFractions(hdrCourse, numFx, plan, TxType):
    dose = rxDose/float(numFx)
    createPlanCheckSet(plan, TxType)
    for i in range(1, int(numFx)+1):
        rxDose = float(hdrCourse.RXDose)
        
        fxNum = int(i)

        print(type(fxNum))
        print(type(dose))
        newFx = HDRFraction.create(hdrCourse, fxNum, dose)
       
        newFx.save()
        createTxCheckSet(newFx, TxType)
        newFx.HDRPlan.add(plan)
        newFx.save()

def createSinglePlanFractions(hdrCourse, numFx, plan, rxDose, TxType):
    createPlanCheckSet(plan, TxType)
    dose = float(rxDose)/float(numFx)
    newFx = HDRFraction.create(hdrCourse, 1, dose)
    newFx.save()
    newFx.HDRPlan.add(plan)    
    newFx.save()

    for i in range(2, int(numFx)+1):
        rxDose = float(hdrCourse.RXDose)
        fxNum = int(i)

        newFx = HDRFraction.create(hdrCourse, fxNum, dose)
       
        newFx.save()
        createTxCheckSet(newFx, TxType)
       

def getPlanAndSave(plan, course):
    Activity =  getRefActivity(plan)
    Kerma = getAirKerma(plan)
    PtName = str(getPtName(plan))

    Time =  getTotalTxTime(plan)
    RxDose = getRxDose(plan)
    refDate =  getReferenceDate(plan)
    planName = getPlanName(plan)
    stepSize = plan.ApplicationSetupSequence[0].ChannelSequence[0].SourceApplicatorStepSize
    loaderName = plan.TreatmentMachineSequence[0].TreatmentMachineName

    plan = HDRPlan.create(course, planName, PtName, RxDose, Time, Kerma, Activity, refDate, loaderName, stepSize)
    plan.save()
    return plan



def getChannelsAndControlPointsAndSave(plan, HDRplan):
   
    channelSet = []
    controlPointSetTotal = []
    for chan in plan.ApplicationSetupSequence[0].ChannelSequence:
        channelIDNumber = chan.ChannelNumber
        numControlPoints = int(chan.NumberOfControlPoints/2)
        channelLength = chan.ChannelLength
        channelTime = chan.ChannelTotalTime
        stepSize = chan.SourceApplicatorStepSize
        channelMapNumber = chan.TransferTubeNumber
        finalTimeWeight = chan.FinalCumulativeTimeWeight
        channel =  Channel.create(HDRplan,  channelIDNumber, channelMapNumber, numControlPoints, stepSize, channelLength, channelTime, finalTimeWeight)
        channel.save()
        controlPointSet = getControlPointsAndSave(plan, chan, channel)
        controlPointSetTotal = controlPointSetTotal + controlPointSet
        channelSet.append(channel)
       
    return channelSet,  controlPointSetTotal   

#def create(cls, channelIDNumber, cPointXpos, cPointYpos, cPointZpos, relativePosition, previousCumTime, cummulativeTime, timeAtPosition, finalTimeWeight)
def getControlPointsAndSave(plan, dicomChannel, channel):
        controlPointSet = []
        previousCumTime = 0

        for i in range(1, len(dicomChannel.BrachyControlPointSequence), 2):
            controlPt  =  dicomChannel.BrachyControlPointSequence[i]
            #channelIDNumber = channel.ChannelNumber 
            controlPtIndex = int((controlPt.ControlPointIndex-1)/2)+1
            cPointXpos =   controlPt.ControlPoint3DPosition[0]
            cPointYpos =   controlPt.ControlPoint3DPosition[1]
            cPointZpos =   controlPt.ControlPoint3DPosition[2]
            relativePostition = controlPt.ControlPointRelativePosition
            cumulativeTimeWeight = controlPt.CumulativeTimeWeight
            channelTime = dicomChannel.ChannelTotalTime
            finalTimeWeight =  dicomChannel.FinalCumulativeTimeWeight
            timeAtPosition = ((cumulativeTimeWeight - previousCumTime)/finalTimeWeight) * channelTime
            controlPoint =  SourceControlPoint.create( channel, controlPtIndex, cPointXpos, cPointYpos, cPointZpos, relativePostition, cumulativeTimeWeight, channelTime, timeAtPosition, finalTimeWeight)
            controlPointSet.append(controlPoint)
            controlPoint.save()
            previousCumTime = cumulativeTimeWeight

        return controlPointSet

def getDosePointsandSave(Plan, hdrPlan):
    doseList = []
    HDRplan = hdrPlan
    for point in Plan.DoseReferenceSequence:

        dosePointX =   float(point.DoseReferencePointCoordinates[0])
        dosePointY =   float(point.DoseReferencePointCoordinates[1])
        dosePointZ =   float(point.DoseReferencePointCoordinates[2])
        print("dose")
       
        dose = float(point.TargetPrescriptionDose)
        
        refNumber = str(point.DoseReferenceNumber)
        print(refNumber)
        dosePoint = DosePoint.create(HDRplan, refNumber, dose, dosePointX, dosePointY, dosePointZ  ) 
        dosePoint.save()
        doseList.append(dosePoint)
    return doseList 



        

        


