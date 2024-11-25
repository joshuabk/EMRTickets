from django.shortcuts import render, redirect

from Patient.models import Patient

import pydicom as pyd

import datetime


from .forms import  dailyQAForm
from .models import  DailyQA 


# Create your views here.
def DailyQA(request):  
     DailyQAForm =  dailyQAForm()
     print("This is the daily QA form.........")
     print(DailyQAForm)
     return render(request, 'DailyQAform.html', {'dailyQAForm': DailyQAForm }) 


def SaveDailyQA(request): 
    if request.method == "POST":        
        DailyQAForm = dailyQAForm(request.POST or None)               
        if DailyQAForm.is_valid():        
            DailyQAForm.save()
           
        
        #dailyQA = DailyQA.objects.all().last()
        
        #dailyQAForm = dailyQAForm(instance = dailyQA)
        
    return render(request, 'DailyQAform.html', {'dailyQAForm':DailyQAForm})
