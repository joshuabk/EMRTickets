from django.db import models

# Create your models here.


from django.db import models

class EMRrequest(models.Model):
    Requestor = models.CharField(max_length=25, null = True)
    EMRSystem = models.CharField(max_length=25, null = True)
    Request = models.CharField(max_length=300, null = True)
    Reason = models.CharField(max_length=300, default = '')
    Priority = models.CharField(max_length=20, default = '')
    Impact = models.CharField(max_length=300, default = '')
    Status = models.CharField(max_length=10, default = 'Pending')
    TimeStamp = models.DateTimeField(auto_now_add=True)
    Comment = models.CharField(max_length=300, default = '')
    ActionTaken = models.CharField(max_length=300, default = '')
    Email = models.EmailField(null = True)
    Phone =  models.CharField(max_length=16, default = '')
    TeamMember  =  models.CharField(max_length=30, default = '')
    DateCompleted = models.DateTimeField(null = True)

    def __str__(self):
        return self.EMRSystem

    


