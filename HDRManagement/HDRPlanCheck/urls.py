
from django.urls import path

from. import views

urlpatterns = [
  
    path('', views.Home, name = 'Home'),
    path('openHDRCourse/', views.openHDRCourse, name = 'openHDRCourse'),
    path('ShowImportedPlan/', views.showImportedPlan, name = 'showImportedPlan'),
    path('Import/', views.importPlan, name = 'importPlan'),
    path('openHDRPlan/<course_id>', views.openHDRPlan, name = 'openHDRPlan'),
    path('deletePatient/<patient_id>', views.deletePatient, name = 'deletePatient'),
    path('deleteHDRCourse/<course_id>', views.deleteHDRCourse, name = 'deleteHDRCourse'),
    path('showHDRPlan/<plan_id>', views.showHDRPlan, name = 'showHDRPlan'),
    path('calcDose/<plan_id>', views.calcDose, name = 'calcDose'),
    path('importPlanToCourse/', views.importPlanToCourse, name = 'importPlanToCourse'),
    path('createCourse/', views.createCourse, name = 'createCourse'),
    path('saveCourse/', views.saveCourse, name = 'saveCourse'),
    path('importPlanFileToCourse/', views.importPlanFileToCourse, name = 'importPlanFileToCourse'),
    path('checkCylinderPlan/<plan_id>', views.checkCylinderPlan, name = 'checkCylinderPlan'),
    path('selectCheckTemps/selectPlanChecksCylinder/', views.selectPlanChecksCylinder, name = 'selectPlanChecksCylinder'),
    path('selectCheckTemps/saveSelectedPlanChecksCylinder/', views.saveSelectedPlanChecksCylinder, name = 'saveSelectedPlanChecksCylinder'),
    path('selectCheckTemps/selectPlanChecksTO/', views.selectPlanChecksTO, name = 'selectPlanChecksTO'),
    path('selectCheckTemps/saveSelectedPlanChecksTO/', views.saveSelectedPlanChecksTO, name = 'saveSelectedPlanChecksTO'),
    
    #path('ImportPlanToCourse/', views.importPlanToCourse, name = 'importPlanToCourse'),

    #path('timeCalc/<slug:slug>', views.TimeCalc, name = 'TimeCalc'),
     
]