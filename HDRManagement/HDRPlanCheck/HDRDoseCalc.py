import datetime
import math
from .models import HDRPlan, HDRCourse, dicomFiles,  SourceControlPoint, Channel, DosePoint

from Patient.models import Patient

RadialDoseData = [[1,1.098], [5,0.9967],[10, 1.0],[20,1.005],[30,1.0075],[40,1.0067], [50,1.0026],[60,0.9955],[70, 0.9854], [80, 0.9724]]

AnositropyFactor = 0.992
DoseRateConstant = 1.109


def getDistanceSourceToDP(CP, DP):
    xDist = CP.CPointXpos - DP.DosePointX
    yDist = CP.CPointYpos - DP.DosePointY
    zDist = CP.CPointZpos - DP.DosePointZ

    totalDistance = math.sqrt(pow(xDist,2) + pow(yDist,2) + pow(zDist,2))
    return totalDistance

def getRadialDoseFactor(rad):
    for i in range(len(RadialDoseData)):
        if RadialDoseData[i][0]< rad and RadialDoseData[i+1][0] > rad:
            interpFactor =  (rad - RadialDoseData[i][0])/(RadialDoseData[i+1][0]-RadialDoseData[i][0])
            radDose = RadialDoseData[i][1] + interpFactor * (RadialDoseData[i+1][1]-RadialDoseData[i][1])
            return radDose

    return 1.0

def CalcDoseRough(time, Kerma, doseRateConstant, anisoFact, rad):
    radialDose = getRadialDoseFactor(rad)
    print("radial dose")
    print(radialDose)
    dose = float(Kerma)/360000.0 * float(doseRateConstant) * float(anisoFact) * float(radialDose) * float(pow(10/rad, 2)) * float(time)
    return dose

#def GetKerma(plan):


def calcTotalDoseForDP(listCP, DP, plan):
    totalDose = 0
    for CP in listCP:

        dist = getDistanceSourceToDP(CP, DP)
        print(CP.TimeAtPosition)
        
        print(dist)
        print(DP.Dose)
        dose = CalcDoseRough(CP.TimeAtPosition, plan.Kerma, DoseRateConstant, AnositropyFactor, dist)
        totalDose += dose
    newTotalDose  =  round(totalDose,4)
    return newTotalDose

def calcDoseError(dosePlan, doseCalc):
    error = round((doseCalc - dosePlan)/dosePlan *100,2)
    return error
