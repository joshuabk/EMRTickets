from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect

from Patient.models import Patient
import pydicom as pyd
import datetime


from .forms import  surveyMeterForm, wellChamberForm
from .models import  SurveyMeter, WellChamber


def addSurveyMeter(request):  
     SurveyMeter = surveyMeterForm()
     print("This is the form................................")
     print(SurveyMeter)
     return render(request, 'AddSurveyMeter.html', {'surveyMeterForm': SurveyMeter }) 

def saveSurveyMeter(request): 
    if request.method == "POST":        
        SurveyMeterForm = surveyMeterForm(request.POST or None)               
        if SurveyMeterForm.is_valid():        
             SurveyMeterForm.save()
        else:
            print("this is invalid")

    meters = SurveyMeter.objects.all()
    print(meters)
    return render(request, 'ShowSurveyMeters.html', {'SurveyMeters': meters })


def showSurveyMeters(request):
     meters = SurveyMeter.objects.all()

     return render(request, 'ShowSurveyMeters.html', {'SurveyMeters': meters })


def deleteSurveyMeter(request,  meter_id):

    delMeter = SurveyMeter.objects.get(pk =  meter_id)
    delMeter.delete()

    return redirect('showSurveyMeters') 

def editSurveyMeter(request,  meter_id):
    if request.method == "POST":
        meter = SurveyMeter.objects.get(pk =meter_id)
        form = saveSurveyMeterForm(request.POST or None, instance=meter)
        print(form.errors)
        if form.is_valid():
            
            messages.success(request, ('Item has been Edited'))
           
            temReq = form.save()
        return render(request, 'ShowSurveyMeters.html', {'SurveyMeters': meters })

    else:  
        editMeter = SurveyMeter.objects.get(pk =  meter_id)#.delete()
        meterForm = surveyMeterForm(instance =  editMeter)

        return render(request, 'AddSurveyMeter.html', {'surveyMeterForm': meterForm})

def addWellChamber(request):  
     WellChamber = wellChamberForm()
     
     print(SurveyMeter)
     return render(request, 'AddWellChamber.html', {'wellChamberForm': WellChamber }) 

def saveWellChamber(request): 
    if request.method == "POST":        
        WellChamberForm = wellChamberForm(request.POST or None)               
        if WellChamberForm.is_valid():        
             WellChamberForm.save()
        else:
            print("this is invalid")

    chambers = WellChamber.objects.all()
    
    return render(request, 'ShowWellChambers.html', {'WellChambers': chambers })


def showWellChambers(request):
     chambers = WellChamber.objects.all()

     return render(request, 'ShowWellChambers.html', {'WellChambers': chambers })


def deleteWellChamber(request,  chamber_id):

    delChamber = WellChamber.objects.get(pk =  chamber_id)
    delChamber.delete()
    return redirect('showWellChambers') 

def editWellChamber(request, chamber_id):
      
   
    editChamber = WellChamber.objects.get(pk =  chamber_id)#.delete()
    ChamberForm = wellChamberForm(instance =  editChamber)

    return render(request, 'AddWellChamber.html', {'wellChamberForm': ChamberForm})




