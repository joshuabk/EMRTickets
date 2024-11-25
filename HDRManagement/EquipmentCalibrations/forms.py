
from django import forms
from .models import SurveyMeter, WellChamber 
import datetime
    




class surveyMeterForm(forms.ModelForm):
    #DoorTest =  models.BooleanField( default = True)
    SurveyMeterName = forms.CharField(label = "Surevey Meter", required = False)
    MeterSN = forms.CharField(label = "Serial Number", required = False)

    CalibrationLab = forms.CharField(label = "Calibration Lab", required = False)

    CalibrationDate =  forms.DateTimeField(label = "Calibration Date", required = False)
    CalibrationDue =  forms.DateTimeField(label = "Calibration Due", required = False)
    CalCerfiticate =  forms.FileField(label = "Calibration Certificate", required = False)

    class Meta:
        model = SurveyMeter 
        fields= ["SurveyMeterName", "MeterSN", "CalibrationLab", "CalibrationDate", "CalibrationDue", "CalCerfiticate"]

class wellChamberForm(forms.ModelForm):
    #DoorTest =  models.BooleanField( default = True)
    Name = forms.CharField(label = "Surevey Meter", required = False)
    SN = forms.CharField(label = "Serial Number", required = False)

    CalibrationLab = forms.CharField(label = "Calibration Lab", required = False)
    CalibrationFactor =  forms.DecimalField(label = "Calibration Factor", required = False)               
    CalibrationDate =  forms.DateTimeField(label = "Calibration Date", required = False)
    CalibrationDue =  forms.DateTimeField(label = "Calibration Due", required = False)
    CalCerfiticate =  forms.FileField(label = "Calibration Certificate", required = False)

    class Meta:
        model = WellChamber
        fields= ["Name", "SN", "CalibrationLab", "CalibrationDate", "CalibrationDue", "CalCerfiticate"]    
