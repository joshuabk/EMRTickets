from django.urls import path

from. import views

urlpatterns = [
     
    path('DailyQA/', views.DailyQA, name = 'DailyQA'),
    path('SaveDailyQA/', views.SaveDailyQA, name = 'SaveDailyQA'),

]