from django.urls import path

from. import views

urlpatterns = [
     
    path('addSurveyMeter/', views.addSurveyMeter, name = 'addSurveyMeter'),
    path('saveSurveyMeter/', views.saveSurveyMeter, name = 'saveSurveyMeter'),
    path('showSurveyMeters/', views.showSurveyMeters, name = 'showSurveyMeters'),
    path('deleteSurveyMeter/<meter_id>', views.deleteSurveyMeter, name = 'deleteSurveyMeter'),
    path('editSurveyMeter/<meter_id>', views.editSurveyMeter, name = 'editSurveyMeter'),
    path('addWellChamber/', views.addWellChamber, name = 'addWellChamber'),
    path('saveWellChamber/', views.saveWellChamber, name = 'saveWellChamber'),
    path('showWellChambers/', views.showWellChambers, name = 'showWellChambers'),
    path('deleteWellChamber/<chamber_id>', views.deleteWellChamber, name = 'deleteWellChamber'),
    path('editWellChamber/<chamber_id>', views.editWellChamber, name = 'editWellChamber'),

]