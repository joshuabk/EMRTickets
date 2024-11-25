from django import forms
from .models import CylinderCheckActivation, TOCheckActivation, CheckSetValuesCylinder, CheckSetValuesTO 
    


class editCylinderCheckActivations(forms.ModelForm):
    ChannelLength = forms.BooleanField(label = "Channel Length", required = False )
    ChannelMapNum = forms.BooleanField(label = "Channel Map Number", required = False, )
    StepSize = forms.BooleanField(label = "Step Size", required = False )
    RxDist = forms.BooleanField(label = "Rx Distance", required = False )
    StepSize = forms.BooleanField(label = "Step Size", required = False )
    RxDose = forms.BooleanField(label = "Rx Dose", required = False, )
    class Meta:
        model = CylinderCheckActivation
        fields= ["ChannelLength", "ChannelMapNum","StepSize","RxDist", "RxDose"]

class editCylinderCheckValues(forms.ModelForm):
    ChannelLengthVal = forms.DecimalField(label = "Channel Length", required = False )
    StepSizeVal = forms.DecimalField(label = "Step Size", required = False)
    MapNumVal = forms.IntegerField(label = "Mapping Number", required = False )
    class Meta:
        model = CheckSetValuesCylinder  
        fields= ["ChannelLengthVal", "StepSizeVal", "MapNumVal"]

class editTOCheckActivations(forms.ModelForm):
    ChannelLength = forms.BooleanField(label = "Channel Length", required = False, )
    StepSize = forms.BooleanField(label = "Step Size", required = False, )
    RxDose = forms.BooleanField(label = "Rx Dose", required = False,)
    class Meta:
        model = TOCheckActivation
        fields= ["RxDose","ChannelLength", "StepSize" ]

class editTOCheckValues(forms.ModelForm):
    ChannelLengthVal = forms.DecimalField(label = "Channel Length", required = False )
    StepSizeVal = forms.DecimalField(label = "Step Size", required = False)
   
    class Meta:
        model = CheckSetValuesTO
        fields= ["ChannelLengthVal", "StepSizeVal"]
    
