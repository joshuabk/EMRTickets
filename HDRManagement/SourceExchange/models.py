from django.db import models

# Create your models here.


# Create your models here.

class SourceExchangeQA(models.Model):
    SourceCertificate = models.FileField(default = "no File")
    QADate = models.DateTimeField(null=True)
    #PrePlanFile = models.FileField(default = "no File")
    DoorTest =  models.BooleanField( default = True)
    EmergencyStopTest = models.BooleanField( default = True)
    PrimeAlertTest = models.BooleanField( default = True)
    IndexerInterlockTest = models.BooleanField( default = True)
    ApplicatorNotInsertedTest = models.BooleanField( default = True)
    PauseTest = models.BooleanField( default = True)
    Completed = models.BooleanField( default = True)

    StatedKerma = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    MeasuredKerma = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    SourceActivity = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    CalculatedActivity = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    
    SourcePositionMeasured = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    SourcePositionProgramed = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    
    SurveyMeter = models.CharField(max_length = 30, null = True)
    SurveyMCalibrationDue = models.DateTimeField(null=True)
    Temperature = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    Pressure = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    
    WellChamber = models.CharField(max_length = 30, null = True)
    WellChamberCalDue = models.DateTimeField(null=True)
    WellChamberCalFactor =  models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    
    Electrometer = models.CharField(max_length = 30, null = True)
    ElectrometerCalDue = models.DateTimeField(null=True)
    ElectrometerCalFactor = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    @classmethod
    def create(cls): 
        SourceExchangeQA = cls() 
        return SourceExchangeQA


class KermaMeasure(models.Model):
        SourceExchangeQA = models.ForeignKey("SourceExchangeQA", on_delete=models.CASCADE, default = 1)
        Temp = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
        Pressure = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
        ElectormeterCal = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
        WellCal = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
        SweetMeaure =  models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
        @classmethod
        def create(cls, sourceExchangeQA ):
            KermaMeasure = cls(SourceExchangeQA = sourceExchangeQA)
            return KermaMeasure

class MeasurePoint(models.Model):
        KermaMeasure = models.ForeignKey("KermaMeasure", on_delete=models.CASCADE, default = 1)
        Measurement = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
        Position =  models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
        @classmethod
        def create(cls, kermaMeaure, measurement, position):
            MeasurePoint = cls(KermaMeaure = kermaMeaure, Measurement = measurement, Position =  position)
            return MeasurePoint

class TimerLinearity(models.Model):
        SourceExchangeQA = models.ForeignKey("SourceExchangeQA", on_delete=models.CASCADE, default = 1)
        Linearity = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
        @classmethod
        def create(cls,  sourceExchangeQA, linearity):
            TimerLinearity = cls ( SourceExchangeQA = sourceExchangeQA, Linearity = linearity )
            return TimerLinearity

class TimeMeasure(models.Model):
        SourceExchangeQA = models.ForeignKey("TimerLinearity", on_delete=models.CASCADE, default = 1)
        SetTime =  models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
        Measurement = models.DecimalField(max_digits = 10,  decimal_places = 2,default = 0)
        @classmethod
        def create(cls,  sourceExchangeQA, setTime, measurement):
            TimerLinearity = cls ( SourceExchangeQA = sourceExchangeQA, SetTime = setTime, Measurement = measurement)
            return TimerLinearity







