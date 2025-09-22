# traffic_api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/data/', views.receive_data, name='receive_data'),
    path('api/analysis/', views.get_analysis_data, name='get_analysis_data'),
]