from django import forms
from .models import  SourceExchangeQA, KermaMeasure, MeasurePoint 
import datetime
    


class sourceExchangeQAForm(forms.ModelForm):
    #SourceCertificate = forms.FileField(default = "no File")
    date = datetime.datetime.now()
    QADate = forms.DateTimeField(label = "Date", initial = date.strftime("%m/%d/%Y   %H:%M:%S"), required = False)
    #PrePlanFile = forms.FileField(default = "no File")
    PauseTest = forms.BooleanField(label = "Pause Test", required = False)
    DoorTest =  forms.BooleanField( label = "Door Interlock", required = False)
    EmergencyStopTest = forms.BooleanField(label = "Emergency Stop", required = False)
    PrimeAlertTest = forms.BooleanField(label = "Prime Alert", required = False)
    IndexerInterlockTest = forms.BooleanField(label = "Indexer Interlockc", required = False)
    ApplicatorNotInsertedTest = forms.BooleanField( label = "Appliator Inserted ", required = False)
   

    StatedKerma = forms.DecimalField(label = "Stated Kerma", required = False)
    MeasuredKerma = forms.DecimalField(label = "Measured Kerma", required = False)
    SourceActivity = forms.DecimalField(label = "Source Activity", required = False)
    CalculatedActivity = forms.DecimalField(label = "Calculated Activity", required = False)
    
    SourcePositionProgramed = forms.DecimalField(label = "Source Position Programed", required = False)
    SourcePositionMeasured =  forms.DecimalField(label = "Source Position Measured", required = False)
    
    SurveyMeter = forms.CharField(label = "Survey Meter", required = False)
    SurveyMCalibrationDue = forms.DateTimeField(label = "Surver Meter Cal Due", required = False)
    Temperature = forms.DecimalField(label = "Temperature", required = False)
    Pressure = forms.DecimalField(label = "Pressure", required = False)
    
    WellChamber = forms.CharField(label = "Well Chamber", required = False)
    WellChamberCalDue = forms.DateTimeField(label = "Well Chamber Cal Due", required = False)
    WellChamberCalFactor =  forms.DecimalField(label = "Well Chamber Cal Factor", required = False)
    
    Electrometer = forms.CharField(label = "Electrometer", required = False)
    ElectrometerCalDue = forms.DateTimeField(label = "Electrometer Cal Due", required = False)
    ElectrometerCalFactor = forms.DecimalField(label = "Electrometer Cal Factor", required = False)
    Completed = forms.BooleanField( label = "Completed", required = False)

    class Meta:
        model = SourceExchangeQA
        fields = [ "QADate","DoorTest",  "EmergencyStopTest", "PauseTest", "SourceActivity", "CalculatedActivity", "StatedKerma", "MeasuredKerma", "SourcePositionMeasured", "SourcePositionProgramed", "SurveyMeter", "SurveyMCalibrationDue", "Temperature", "Pressure", "WellChamber", "WellChamberCalDue", "WellChamberCalFactor", "Electrometer", "ElectrometerCalDue" , "ElectrometerCalFactor", "IndexerInterlockTest","ApplicatorNotInsertedTest", "ApplicatorNotInsertedTest", "EmergencyStopTest","PrimeAlertTest", "Completed"] 

class KermaMeasureForm(forms.ModelForm):
        #SourceExchange = forms.ForeignKey("SourceExchangeQA", on_delete=models.CASCADE, default = 1)
        Temp = forms.DecimalField(label = "Temperature", required = False)
        Pressure =forms.DecimalField(label = "Pressure", required = False)
        ElectrometerCal =forms.DecimalField(label = "Electrometer Calibration", required = False)
        WellCal =forms.DecimalField(label = "Chamber Calibration", required = False)
        
        class Meta:
            model = KermaMeasure
        
            fields = [ "Temp" , "Pressure", "ElectrometerCal", "WellCal"]
            

class MeasurePointForm(forms.ModelForm):
        #KermaMeasure = models.ForeignKey("KermaMeasure", on_delete=models.CASCADE, default = 1)
        Measurement =forms.DecimalField(label = "Reading", required = False)
        Position = forms.DecimalField(label = "Position", required = False)
        class Meta:
            model = MeasurePoint
            fields = [ "Position","Measurement" ]
            