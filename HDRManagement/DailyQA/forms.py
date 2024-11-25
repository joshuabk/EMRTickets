
from django import forms
from .models import DailyQA 
from EquipmentCalibrations.models import SurveyMeter
import datetime
    

class dailyQAForm(forms.ModelForm):
    date = datetime.datetime.now()
    QATestDate = forms.DateTimeField( label = "Date", initial = date.strftime("%m/%d/%Y   %H:%M:%S"), required = False)
    #PrePlanFile = models.FileField(default = "no File")
    DoorTest =  forms.BooleanField(label = "Door Interlock", required = False )
    EmergencyStopTest = forms.BooleanField(label = "Emergency Stop", required = False)
    StartUpTest = forms.BooleanField(label = "Start Up Test", required = False )
    PauseTest = forms.BooleanField(label = "Pause Test", required = False)
    SourceActivity = forms.DecimalField(label = "Source Activity", required = False)
    CalculatedActivity = forms.DecimalField(label = "Calculated Activity", required = False)
    StopWatchTimer = forms.DecimalField(label = "Stopwatch Time", required = False )
    SourcePositionMeasured = forms.DecimalField(label = "Source Position Measured", required = False)
    SourcePositionProgramed = forms.DecimalField(label = "Source Position Programed", required = False )
    SurveyMeter = forms.ModelChoiceField(queryset=SurveyMeter.objects.all(), initial=0)
    
    SurveyMCalibrationDue = forms.DateTimeField(widget = forms.SelectDateWidget, label = "Calibration Due", required = False)
    Completed =forms.BooleanField( label = "Completed",  required = False )
    #def get_initial(self):
        # call super if needed
        #return {'SurveyMCalibrationDue': datetime.datetime.now()}

   
    class Meta:
        model = DailyQA
        fields= ["QATestDate", "DoorTest", "EmergencyStopTest", "StartUpTest", "PauseTest", "Completed", "SourceActivity", "CalculatedActivity", "StopWatchTimer", "SourcePositionMeasured", "SourcePositionProgramed", "SurveyMeter", "SurveyMCalibrationDue"]