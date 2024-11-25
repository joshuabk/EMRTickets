from django import forms
from .models import EMRrequest
from datetime import datetime

class requestForm(forms.ModelForm):
    Impact = forms.CharField(required=False)
    Email = forms.CharField(required=False)
    class Meta:
        model = EMRrequest
        fields= ["Requestor", "EMRSystem", "Request", "Reason", "Priority", "Impact", "Email", "Phone"]

class editRequestForm(forms.ModelForm):
    Comment = forms.CharField(required=False)
    Impact = forms.CharField(required=False)
    Email = forms.CharField(required=False)
    TeamMember = forms.CharField(required=False)
    Phone = forms.CharField(required=False)
    ActionTaken = forms.CharField(required=False)
    DateCompleted = forms.DateTimeField(required=False)

    class Meta:
        model = EMRrequest
        fields= ["Requestor", "EMRSystem", "Request", "Reason", "Priority", "Impact", "Status", "Comment", "Email", "Phone","TeamMember", "ActionTaken", "DateCompleted"]
    
  