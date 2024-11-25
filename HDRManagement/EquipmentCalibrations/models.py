from django.db import models

# Create your models here.


# Create your models here.

class SurveyMeter(models.Model):
    #DoorTest =  models.BooleanField( default = True)
    SurveyMeterName = models.CharField(max_length = 30, null = True)
    MeterSN = models.CharField(max_length = 30, null = True)

    CalibrationLab = models.CharField(max_length = 30, null = True)

    CalibrationDate =  models.DateTimeField(null=True)
    CalibrationDue =  models.DateTimeField(null=True)
    CalCerfiticate =  models.FileField(null=True)

    @classmethod
    def create(cls, surveyMeterName, meterSN, calibrationLab, calibrationDate, calibrationDue, calCerfiticate): 
        SurveyMeter = cls(SurveyMeterName = surveyMeterName, CalibrationLab = calibrationLab, CalibrationDate = calibrationDate, CalibrationDue = calibrationDue, CalCerfiticate = calCerfiticate)
        return SurveyMeter


class WellChamber(models.Model):
    #DoorTest =  models.BooleanField( default = True)
    Name = models.CharField(max_length = 30, null = True)
    SN = models.CharField(max_length = 30, null = True)

    CalibrationLab = models.CharField(max_length = 30, null = True)
    CalibrationFactor =  models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    CalibrationDate =  models.DateTimeField(null=True)
    CalibrationDue =  models.DateTimeField(null=True)
    CalCerfiticate =  models.FileField(null=True)

    @classmethod
    def create(cls, surveyMeterName, SN, calibrationLab, calibrationDate, calibrationDue, calibrationFactor, calCerfiticate): 
        WellChamber = cls(Name = name, SN = SN, CalibrationLab = calibrationLab, CalibrationDate = calibrationDate, CalibrationDue = calibrationDue,  CalibrationFactor = calibrationFactor, CalCerfiticate = calCerfiticate)
        return WellChamber

