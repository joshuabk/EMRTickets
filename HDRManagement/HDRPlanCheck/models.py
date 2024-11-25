from django.db import models

from Patient.models import Patient

# Create your models here.


class HDRCourse(models.Model):
    CourseName =  models.CharField(max_length = 30,  default = 'HDR')
    Patient = models.ForeignKey("Patient.Patient", on_delete=models.CASCADE, default = "John")
    PatientName =  models.CharField(max_length = 30,  default = 'HDR')
    NumFractions =  models.IntegerField(default=0)
    CourseType =  models.CharField(max_length = 30,  default = 'HDR')
    TxType =  models.CharField(max_length = 30,  default = 'Cyl')
    RXDose = models.DecimalField(max_digits = 10, decimal_places = 3, default = 0 )
    RXDist = models.DecimalField(max_digits = 10, decimal_places = 3, default = 0 )
    Active = models.BooleanField(default = True)
    
    class Meta:
        unique_together = ('PatientName', 'CourseName',)
    @classmethod
    def create(cls, courseName, patient, patientName, courseType, rxDose, rxDist, numFractions, txType):
        course = cls(CourseName =  courseName, Patient =  patient, PatientName =  patientName, CourseType = courseType, RXDose = rxDose, RXDist = rxDist, NumFractions = numFractions, TxType =  txType)

        return course

class HDRFraction(models.Model):
     HDRCourse = models.ForeignKey("HDRCourse", on_delete=models.CASCADE, default = "HDR")
     HDRPlan = models.ManyToManyField("HDRPlan", default = 1)
     PlanFile = models.FileField(null = True)
     FxNum = models.IntegerField(default=0)
     Acivity = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
     Dose = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
     TxTime = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
     Date = models.DateField(null = True)
     @classmethod
     def create(cls, hdrCourse, fxNum, dose):
        fraction = cls(HDRCourse =  hdrCourse, FxNum = fxNum, Dose = dose)
        return fraction

class HDRPlan(models.Model):
    Site = models.CharField(max_length = 100, blank=True)
    Course = models.ForeignKey("HDRCourse", on_delete=models.CASCADE, default = 1)
    Fraction = models.ManyToManyField("HDRFraction")
    TxType = models.CharField(max_length = 20, null = True)
    PatientName = models.CharField(max_length = 30, null = True)
    PlanName = models.CharField(max_length = 30,  default = 'HDR')
    LoaderName = models.CharField(max_length = 30, blank=True)
    Isotope =  models.CharField(max_length = 30, blank=True)
    Rx_dose = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    Kerma =  models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    PlanActivity =  models.DecimalField(max_digits = 10, decimal_places = 3, default = 0 )
    CurrActivity = models.DecimalField(max_digits = 10, decimal_places = 3, null = True )
    RefDate = models.DateTimeField(null=True)
    Time = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
    dicomFile = models.FileField()
    StepSize =  models.DecimalField(max_digits = 10, decimal_places = 2, default = 0, null = True)
    NumFx = models.IntegerField(null=True)
    PlanOptimization = models.CharField(max_length = 30, blank=True)
    PlanNormalization = models.CharField(max_length = 30, blank=True)
    class Meta:
        unique_together = ('Course', 'PlanName')

    @classmethod
    def create(cls, course, planName, patientName, rx_dose, time, kerma, planActivity, refDate, loaderName, stepSize):
        plan = cls(Course =  course, PlanName = planName, PatientName = patientName,Rx_dose = rx_dose, Time = time, Kerma = kerma, PlanActivity = planActivity, RefDate = refDate, LoaderName = loaderName, StepSize = stepSize )

        return plan

class Channel(models.Model):
    Plan = models.ForeignKey("HDRPlan", on_delete=models.CASCADE, default = 1)
    ChannelIDNumber = models.IntegerField(default=0)
    ChannelMapNumber = models.IntegerField(default=0)
    StepSize =  models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    ChannelLength = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    ChannelTime  = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    NumberOfControlPoints = models.IntegerField(default=0)
    FinalTimeWeight = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    @classmethod
    def create(cls, plan, channelIDNumber, channelMapNumber, numberOFControlPoints, stepSize, channelLength, channelTime, finalTimeWeight):
        channel =  cls(Plan =  plan, ChannelIDNumber = channelIDNumber, ChannelMapNumber= channelMapNumber, NumberOfControlPoints = numberOFControlPoints, StepSize = stepSize, ChannelLength = channelLength, ChannelTime = channelTime, FinalTimeWeight = finalTimeWeight)
        return channel
        
class SourceControlPoint(models.Model):
    Channel = models.ForeignKey("Channel", on_delete=models.CASCADE, default = 1)
    CPointXpos = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    CPointYpos = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    CPointZpos = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    ControlPtIndex = models.IntegerField(default=0)
    RelativePosition = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    PreviousCumTime = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    CummulativeTime =  models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    TimeAtPosition =  models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    FinalTimeWeight = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    @classmethod
    def create(cls, channel, controlPointIndex, cPointXpos, cPointYpos, cPointZpos, relativePosition, previousCumTime, cummulativeTime, timeAtPosition, finalTimeWeight):
        sourcePoint = cls(Channel = channel, ControlPtIndex = controlPointIndex,  CPointXpos = cPointXpos, CPointYpos = cPointYpos, CPointZpos = cPointZpos, PreviousCumTime = previousCumTime, CummulativeTime = cummulativeTime, TimeAtPosition = timeAtPosition, FinalTimeWeight = finalTimeWeight)
        return sourcePoint


class dicomFiles(models.Model):
    PlanName = models.ForeignKey("HDRPlan", on_delete=models.CASCADE, default = 1)
    dicomFile = models.FileField()

    def __str__(self):
        return self.dicomFile

class tempPlanFile(models.Model):
    TempFile = models.FileField(default = "no File")
    @classmethod
    def create(cls, tempFile):
        tempPlanFile = cls(TempFile = tempFile)
        return tempPlanFile


class HDRPlanCheckSet(models.Model):
    Plan = models.OneToOneField("HDRPlan", on_delete=models.CASCADE, unique = True, default = 1)
    CheckType =  models.CharField(max_length = 30, blank=True)
    @classmethod
    def create(cls, plan, checkType):
            HDRPlanCheckSet = cls(Plan = plan,  CheckType = checkType)
            return HDRPlanCheckSet


class HDRPlanCheck(models.Model):
    PlanCheckSet = models.ForeignKey("HDRPlanCheckSet", on_delete=models.CASCADE, default = 1)
    Name = models.CharField(max_length = 30, blank=True)
    PlanType =  models.CharField(max_length = 30, blank=True)
    CheckDescription =  models.CharField(max_length = 120, blank=True)
    Result  = models.CharField(max_length = 30, blank=True)
    Value = models.CharField(max_length = 30, blank=True)
    ExpectedValue = models.CharField(max_length = 30, blank=True)
    PlanNormalization = models.BooleanField(default = True)
    @classmethod
    def create(cls, name,  planCheckSet, planType, checkDescription, result, value, expectedValue):
        HDRplanCheck = cls(Name = name, PlanCheckSet = planCheckSet, PlanType = planType, CheckDescription =checkDescription, Result = result, Value = value, ExpectedValue = expectedValue)
        return HDRplanCheck

class CheckSetValuesCylinder(models.Model):
    ChannelLengthVal = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    StepSizeVal = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    MapNumVal = models.IntegerField(default=0)

class CheckSetValuesTO(models.Model):
    ChannelLengthVal = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
    StepSizeVal = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
   
class HDRTxCheckSet(models.Model):
     HDRFraction = models.ForeignKey("HDRFraction", on_delete=models.CASCADE, default = 1)
     FxNum = models.IntegerField(default=0)
     CheckType =  models.CharField(max_length = 30, blank=True)
     Acivity = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
     Dose = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
     TxTime = models.DecimalField(max_digits = 10, decimal_places = 2,default = 0)
     @classmethod
     def create(cls, fraction, checkType):
            HDRTxCheckSet = cls(HDRFraction = fraction,  CheckType = checkType)
            return HDRTxCheckSet

#selects which checks to use for cylinder plan

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

class CylinderCheckActivation(models.Model):  
    ChannelLength = models.BooleanField( default = True)
    ChannelMapNum = models.BooleanField( default = True)
    StepSize =  models.BooleanField( default = True)
    RxDist =  models.BooleanField( default = True)
    RxDose =  models.BooleanField( default = True)
    PlanNormalization = models.BooleanField( default = True)
    PlanOptimization = models.BooleanField(default = True)
    CheckTxUnit = models.BooleanField(default = True)
    ChannelNum = models.BooleanField(default = True)
    CheckDosePointDistance = models.BooleanField( default = True)
    @classmethod
    def create(cls):
        activationListCylinder = cls()
        return activationListCylinder

class TOCheckActivation(models.Model):  
    ChannelLength = models.BooleanField( default = True)
    StepSize =  models.BooleanField( default = True)
    RxDose =  models.BooleanField( default = True)
    PlanNormalization = models.BooleanField( default = True)
    PlanOptimization = models.BooleanField(default = True)
    CheckTxUnit = models.BooleanField(default = True)
    ChannelNum = models.BooleanField(default = True)
    CheckDosePointDistance = models.BooleanField( default = True)
    @classmethod
    def create(cls):
        activationListTO = cls()
        return activationListTO


class DosePoint(models.Model):   
    HDRPlan = models.ForeignKey("HDRPlan", on_delete=models.CASCADE, default = 1)
    DosePointX = models.DecimalField(max_digits = 10, decimal_places = 3,default = 0)
    DosePointY = models.DecimalField(max_digits = 10, decimal_places = 3,default = 0)
    DosePointZ = models.DecimalField(max_digits = 10, decimal_places = 3,default = 0)
    Dose = models.DecimalField(max_digits = 10, decimal_places = 4,default = 0)
    RefNumber = models.CharField(max_length = 5, blank=True)
    @classmethod
    def create(cls, plan, refNumber, dose, dosePointX, dosePointY, dosePointZ):
        dosePoint = cls(HDRPlan = plan, RefNumber = refNumber, Dose = dose,  DosePointX = dosePointX, DosePointY = dosePointY, DosePointZ = dosePointZ)
        return dosePoint