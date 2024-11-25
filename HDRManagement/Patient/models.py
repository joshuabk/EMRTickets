from django.db import models

# Create your models here.

class Patient(models.Model):
    PatientName =  models.CharField(max_length = 30 )
    PatientDOB =  models.DateField(max_length = 20, null = True)
    PatientID = models.CharField(max_length = 30, primary_key= True)
    @classmethod
    def create(cls, patientName, patientDOB, patientID):
        patient = cls(PatientName = patientName, PatientDOB= patientDOB, PatientID = patientID)

        return patient


