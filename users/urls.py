from django import views
from django.urls import path

from users.views import RegistrationApi



urlpatterns = [
    path('RegistrationApi', RegistrationApi.as_view(), name='RegistrationApi'),
   
]