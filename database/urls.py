from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume, name='resume'),
    path('request_data/', views.dataquery, name='request_data')
]