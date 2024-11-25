import datetime
import math
from .models import HDRPlan, HDRCourse, dicomFiles,  SourceControlPoint, Channel, DosePoint, HDRPlanCheck, CylinderCheckActivation, TOCheckActivation

from Patient.models import Patient

def createCylinderCheckSet(plan, planCheckSet, RXDist):
        DPList = getDPlist(plan)
        CPList = getCPlist(plan)
        ChannelList = getChannelList(plan)
        #actList = CylinderCheckActivation.create()
        #actList.save()
        activationList = CylinderCheckActivation.objects.all().first()  
        
        if(activationList.ChannelLength):
            CheckChannelLengthsIs1500(ChannelList, planCheckSet)
        if(activationList.ChannelMapNum):
            CheckCylinderChannelNucMapping(ChannelList[0], planCheckSet)

        if(activationList.StepSize):
            CheckStepSize(ChannelList[0],  planCheckSet)
        if(activationList.RxDist):
            checkDPRXDistance(RXDist, CPList, DPList, planCheckSet)
        if(activationList.RxDose):
            CheckRxDoseCylinder(plan,  planCheckSet)
        return planCheckSet

def createTOCheckSet(plan, planCheckSet):
        DPList = getDPlist(plan)
        CPList = getCPlist(plan)
        ChannelList = getChannelList(plan)
        #actList = CylinderCheckActivation.create()
        #actList.save()
        activationList = TOCheckActivation.objects.all().first()  
        
        if(activationList.ChannelLength):
            CheckChannelLengthsIs1500(ChannelList, planCheckSet)

        if(activationList.StepSize):
            CheckStepSize(ChannelList[0],  planCheckSet)
        
        if(activationList.RxDose):
            CheckRxDoseCylinder(plan,  planCheckSet)
        return planCheckSet

def CheckChannelLengthsIs1500(ChannelList, planCheckSet):
    channelsPass = True
    for channel in ChannelList:
        if channel.ChannelLength != 1500.0:
            channelsPass = False
    name = "channel lengths"
    planType = "All"
    
    value = channel.ChannelLength
    expectedValue = 1500
    checkDescription = "Channel Lengths are corrrect "
    if(channelsPass):
        result = "Pass"
    else:
        result = "Fail"
    planCheck = HDRPlanCheck.create(name,  planCheckSet, planType, checkDescription, result, value, expectedValue)
    planCheck.save()    
    return channelsPass
    
def CheckCylinderChannelNucMapping(channel, planCheckSet):
    mappingPass = True
    
    expectedValue = 3
    name = "Channel Mapping"
    planType = "Clyinder"
   
    value = channel.ChannelMapNumber
    checkDescription = "Channel Mapping is correct"
    mappingPass = value == expectedValue
    if(mappingPass):
        result = "Pass"
    else:
        result = "Fail"
    planCheck = HDRPlanCheck.create(name, planCheckSet, planType, checkDescription, result, value, expectedValue)
    planCheck.save()  

def CheckStepSize(channel,  planCheckSet):
    stepPass = True
    stepSize = channel.StepSize        
    name = "StepSize"
    planType = "All"
   
    value =  channel.StepSize
    expectedValue = 2.5
    stepPass = value == expectedValue
    checkDescription = "Check that step size is correct "
    if(stepPass):
        result = "Pass"
    else:
        result = "Fail"
    planCheck = HDRPlanCheck.create(name, planCheckSet, planType, checkDescription, result, value, expectedValue)
    planCheck.save()

def CheckRxDoseCylinder(plan, planCheckSet):
    stepPass = True
            
    name = "Rx Check"
    planType = "All"
   
    value =  float(plan.Rx_dose)
    expectedValue = float(plan.Course.RXDose)/float(plan.Course.NumFractions)
    stepPass = value == expectedValue
    checkDescription = "Check that course Rx mathches plan Rx "
    if(stepPass):
        result = "Pass"
    else:
        result = "Fail"
    planCheck = HDRPlanCheck.create(name, planCheckSet, planType, checkDescription, result, value, expectedValue)
    planCheck.save()

def getDistanceSourceToDP(CP, DP):
    xDist = CP.CPointXpos - DP.DosePointX
    yDist = CP.CPointYpos - DP.DosePointY
    zDist = CP.CPointZpos - DP.DosePointZ

    totalDistance = math.sqrt(pow(xDist,2) + pow(yDist,2) + pow(zDist,2))
    return totalDistance 

def getMiniumDistanceDPsToCPs(DPList, CPList):
    minDist = 10000000
    for DP in DPList: 
        for CP in CPList:
            dist = getDistanceSourceToDP(CP, DP)
            if dist < minDist:
                minDist = dist
    return round(minDist, 3)

def checkDPRXDistance(RXDist, CPList, DPList, planCheckSet):

    passing = True
    DPDist = getMiniumDistanceDPsToCPs(DPList, CPList)
    if DPDist > float(RXDist) * 1.02 or  float(DPDist) < float(RXDist) * 0.98:
        passing = False
    name = "RXDistanceCheck"
    planType = "Cylinder"

    expectedValue = RXDist
    value = DPDist
    checkDescription = "Check that dose is prescribed to the correct distance"
    if(passing):
        result = "Pass"
    else:
        result = "Fail"
    planCheck = HDRPlanCheck.create(name, planCheckSet, planType, checkDescription, result, value, expectedValue)
    planCheck.save()


def getDPlist(plan):
    DPlist = list(DosePoint.objects.filter(HDRPlan = plan))
    return DPlist

def getCPlist(plan):
    channelSet = Channel.objects.filter(Plan = plan)
    channel = channelSet.first()
    CPlist = list(SourceControlPoint.objects.filter(Channel = channel))
    return CPlist

    

def getChannelList(plan):
    ChannelList = list(Channel.objects.filter(Plan = plan))
    return ChannelList

    
    


