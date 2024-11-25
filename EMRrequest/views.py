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

   



# Create your views here.




def addRequest(request):
    
    if request.method == "POST":
        form = requestForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been Added to the list!'))
            print('send mail')

            connection = mail.get_connection()
            print(connection)
            '''if isinstance(connection, EmailBackend):
                connection.open()
                print("connection is open")'''
             
               
           
            body = 'The new request from '+ request.POST.get('Requestor')+' is as follows: \n\n EMR System: '+  request.POST.get('EMRSystem')+'\n \n Request: '+ request.POST.get('Request')+'  \n\n Reason: '+ request.POST.get('Reason')+'\n\n Priority: '+  request.POST.get('Priority')+'\n\n Impact: '+  request.POST.get('Impact') +'\n\nHere is the link to the EMR Request page http://10.40.71.201:2000/'  
            
            print(body)
            email = EmailMessage(
                  'New EMR Change Request',
                   body,
                    settings.EMAIL_HOST_USER,
                   ['joshua.kessler@northside.com', 'RadiationOncologyEMR@northside.com',])
            

            email.send()
            print('mail sent')

            
            return render(request, 'requestSuccess.html', {})
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
            else:
                temReq.save()

            requests = list(EMRrequest.objects.all())
            
            
            return redirect('showActiveRequests')
        else:
           
            print("Farts")
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







