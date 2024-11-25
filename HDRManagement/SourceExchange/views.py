from django.shortcuts import render, redirect

from Patient.models import Patient

import pydicom as pyd
import datetime
from django.forms import formset_factory

from .forms import  sourceExchangeQAForm, KermaMeasureForm, MeasurePointForm
from .models import  SourceExchangeQA, KermaMeasure


def SourceExchange(request):  
     exchange = SourceExchangeQA.create()
     exchange.save()
     SourceExchangeForm =  sourceExchangeQAForm(instance = exchange)
     kermaM =  KermaMeasure.create(exchange)
     kermaM.save()

    
     return render(request, 'SourceExchange.html', {'sourceExchangeForm': SourceExchangeForm, 'kermaM':kermaM}) 

def SourceExchangeReturn(request):  
     #exchange = SourceExchangeQA.objects.get(pk = exchange_id)
     SourceExchangeForm =  sourceExchangeQAForm(instance = exchange)
     
    
     return render(request, 'SourceExchange.html', {'sourceExchangeForm': SourceExchangeForm}) 

def saveSourceExchange(request, kerma_id): 
    if request.method == "POST": 

        SourceExchangeForm = sourceExchangeQAForm(request.POST or None)               
        if SourceExchangeForm.is_valid():  
            print("iiiitts vallllliiiiddd        d")      
            sourceExhange = SourceExchangeForm.save() 
        else:
            print("n oooooooooooooooo    iiiitts vallllliiiiddd")
            print(len(SourceExchangeForm.errors))
            print(SourceExchangeForm.errors)
            #sourceExhange = SourceExchangeForm.save()
        #dailyQA = DailyQA.objects.all().last()
        
        #dailyQAForm = dailyQAForm(instance = dailyQA)
        
        
    return render(request, 'KermaMeasurement.html', {'SourceExchange': sourceExhange})

def KermaMeasureView(request, kermaM_id):  
     
     
     print(kermaM_id)
     kerma1 =  KermaMeasure.objects.get(pk = kermaM_id)
     
     kermaForm1 = KermaMeasureForm(instance = kerma1)
     measureSet =  formset_factory(MeasurePointForm, extra = 3)
     #measureSet =  measureSetInit(initial = {"KermaMeasure" : kerma1})
     #formSet = measureSet(initial = {'KermaMeasure': kermaForm1})
     
     return render(request, 'KermaMeasurement.html', {'KermaMeasureForm1': kermaForm1, 'MeasureSet1': measureSet })

def saveKermaMeasure(request):
    if request.method == "POST":        
        KermaMeasureF = KermaMeasureForm(request.POST or None) 
                     
        if KermaMeasureF.is_valid():        
            kermaMeaureInst = KermaMeasureF.save()
            measureSet =  formset_factory(MeasurePointForm,  extra = 3)
           

            formSet = measureSet(request.POST or None)
            if formSet.is_valid():
            
                for form in formSet:
                    measure = form.save(commit = False)
                    measure.KermaMeasure = kermaMeaureInst
                    measure.save()

    return render(request, 'KermaMeasurement.html',{})



       
        
        #dailyQA = DailyQA.objects.all().last()
        
        #dailyQAForm = dailyQAForm(instance = dailyQA)
        
    #return render(request, 'SourceExchange.html', {'sourceExchangeForm':SourceExchangeForm}) 
