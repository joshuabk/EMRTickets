
from django.urls import path
from . import views
urlpatterns = [
    path('', views.addRequest, name='addRequest'),
    path('login/',  views.loginUser, name = 'login' ),
    path('logout/',  views.logoutUser, name = 'logout' ),
    path('showActiveRequests/', views.showActiveRequests, name='showActiveRequests'),
    path('showAllRequests/', views.showAllRequests, name='showAllRequests'),
    path('editRequest/<int:request_id>', views.editRequest, name='editRequest'),
    path('deleteRequest/<request_id>',views.deleteRequest, name='deleteRequest'),  
   
]