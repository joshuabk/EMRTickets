from django.db import models


# Create your models here.

class DailyQA(models.Model):
    QATestDate = models.DateTimeField(null=True)
    #PrePlanFile = models.FileField(default = "no File")
    DoorTest =  models.BooleanField( default = True)
    EmergencyStopTest = models.BooleanField( default = True)
    StartUpTest =  models.BooleanField( default = True)
    PauseTest = models.BooleanField( default = True)
    
    SourceActivity = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    CalculatedActivity = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    StopWatchTimer = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)

    SourcePositionMeasured =  models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    SourcePositionProgramed =  models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    SurveyMeter = models.CharField(max_length = 30, null = True)
    SurveyMCalibrationDue = models.DateTimeField(null=True)
    Completed = models.BooleanField( default = True)

    @classmethod
   
    def create(cls, qaTestDate, doorTest, emergencyStopTest, startUpTest, pauseTest, completed, sourceActivity, calculatedActivity, stopWatchTimer,sourcePositionMeasured, sourcePositionProgramed, surveyMeter, surveyMCalibrationDue): 
        dailyQA = cls(QATestDate = qaTestDate, DoorTest = doorTest, EmergencyStopTest = emergencyStopTest, StartUpTest = startUpTest, PauseTest = pauseTest, Completed = completed, SourceActivity = sourceActivity, CalculatedActivity = calculatedActivity, StopWatchTimer = stopWatchTimer, SourcePositionMeasured = sourcePositionMeasured, SourcePositionProgramed = sourcePositionProgramed, SurveyMeter = surveyMeter, SurveyMCalibrationDue = surveyMCalibrationDue)
        return dailyQA

