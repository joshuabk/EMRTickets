
from django.urls import path

from. import views

urlpatterns = [
    path('SourceExchange/', views.SourceExchange, name = 'SourceExchange'),
    path('SourceExchangeReturn/<exchange_id>', views.SourceExchangeReturn, name = 'SourceExchangeReturn'),
    path('saveSourceExchange/<kerma_id>', views.saveSourceExchange, name = 'saveSourceExchange'),
    path('KermaMeasureView/<kermaM_id>', views.KermaMeasureView, name = 'KermaMeasureView'),
    path('saveKermaMeasure/', views.saveKermaMeasure, name = 'saveKermaMeasure'),

]