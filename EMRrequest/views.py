from django.shortcuts import render, redirect
from .models import EMRrequest 
from .forms import requestForm, editRequestForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages 

from django.core.mail import send_mail, EmailMessage
from django.conf import settings

from smtplib import SMTPException
from datetime import datetime

from django.core import mail
from django.core.mail.backends.smtp import EmailBackend

import tkinter as tk

from tkinter import messagebox



   



# Create your views here.

#admin login
#joshuabk, physics1


def addRequest(request):
    
    if request.method == "POST":
        form = requestForm(request.POST or None)

        if form.is_valid():
            req = form.save()
            messages.success(request, ('Item has been Added to the list!'))
            print('send mail')

          
            '''connection = mail.get_connection()
            print(connection)
                if isinstance(connection, EmailBackend):
                connection.open()
                print("connection is open")
             
               
            body = 'The new request from '+ request.POST.get('Requestor')+' is as follows: \n\n EMR System: '+  request.POST.get('EMRSystem')+'\n \n Request: '+ request.POST.get('Request')+'  \n\n Reason: '+ request.POST.get('Reason')+'\n\n Priority: '+  request.POST.get('Priority')+'\n\n Impact: '+  request.POST.get('Impact') +'\n\nHere is the link to the EMR Request page http://167.183.14.241:2000/'  
            
            body2 = 'The new request from '+ request.POST.get('Requestor')+' is as follows: \n\n EMR System: '+  request.POST.get('EMRSystem')+'\n \n Request: '+ request.POST.get('Request')+'  \n\n Reason: '+ request.POST.get('Reason')+'\n\n Priority: '+  request.POST.get('Priority')+'\n\n Impact: '+  request.POST.get('Impact')   
            print(body)
            email = EmailMessage(
                  'New EMR Change Request',
                   body,
                   settings.EMAIL_HOST_USER,
                   ['Ashley.davis2@northside.com', 'Laura.NkwentiBimbo@northside.com','Debra.Corbin@northside.com','Mrugesh.Patel@northside.com', 'Terror.Ragland@northside.com','Tomi.Ogunleye@northside.com', 'Gina.Kellogg@northside.com', 'Alisha.Childs@northside.com','Darlene.ritarita@northside.com','Camille.smith2@northside.com','Ashley.Chackalayil@northside.com','RadiationOncologyEMR@northside.com'])
            
           
            email.send()
            

            email2 = EmailMessage(
                  'EMR Change Request Confirmation',
                   body2,
                    settings.EMAIL_HOST_USER,
                   ['Joshua.Kessler@northside.com', request.POST.get('Email')])

            email2.send()

           

           

            print('mail sent')'''

            
            return render(request, 'requestSuccess.html', {'requestID': req.pk})
        else:
            messages.error(request, "Error")
            return render(request, 'request.html', {'errors': form.errors})

    else:
        return render(request, 'request.html', {})


def showActiveRequests(request):
   
    orderBy = request.GET.get('order_by', '-TimeStamp')
    requests = EMRrequest.objects.all().order_by(orderBy)
    return render(request, 'showActiveRequests.html', {'requests':requests})

def showAllRequests(request):
    orderBy = request.GET.get('order_by', '-TimeStamp')
    requests = EMRrequest.objects.all().order_by(orderBy)
    return render(request, 'showAllRequests.html', {'requests':requests})


def deleteRequest(request, request_id):
    deleteRequest = EMRrequest.objects.get(pk = request_id)
    deleteRequest.delete()
    requests = EMRrequest.objects.all
    return redirect('showActiveRequests')


def editRequest(request, request_id):
    if request.method == "POST":
        requestEMR = EMRrequest.objects.get(pk = request_id)
        form = editRequestForm(request.POST or None, instance=requestEMR)
        print(form.errors)
        if form.is_valid():
            
            messages.success(request, ('Item has been Edited'))
           
            temReq = form.save(commit = False)

            if temReq.Status =="Complete" and  temReq.DateCompleted ==None:
                temReq.DateCompleted = datetime.now()
                temReq.save()
               
                #root.withdraw()
                confirmMessage = "Dear "+requestEMR.Requestor+",\n \n Your EMR Change request #"+ str(requestEMR.pk)+ " has been resolved \n\n Request: "+ requestEMR.Request+"\n \n Action Taken: "+requestEMR.ActionTaken+"\n \n Thanks, \n "+ requestEMR.TeamMember
                email = EmailMessage(
                  'EMR Change Request Completion Message',
                   confirmMessage,
                    settings.EMAIL_HOST_USER,
                   [requestEMR.Email])
            
           
                #email.send()
            else:
                temReq.save()
                print("save doont complete")

            requests = list(EMRrequest.objects.all())
            
            
            return redirect('showActiveRequests')
        else:
           
            print("Form is not Valid")
            messages.error(request, "Error")
            requests = EMRrequest.objects.all
            return redirect('showActiveRequests')
           
    else:
        
        requestEMR = EMRrequest.objects.get(pk = request_id)
        return render(request, 'editRequest.html', {'request':requestEMR})


def loginUser(request):
    if request.method == 'POST':
        password = request.POST.get("password")
        username = request.POST.get("username")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, ('Login Successful'))
            return redirect(showActiveRequests)


            
        else:
            messages.success(request, ('Error, please try again'))
            return redirect('login')

    else:
        
        
        return render(request, 'login.html', {})

def logoutUser(request):
    logout(request)
    messages.success(request, ('You have Been Logged Out'))
    return redirect('login')







