from django import views
from django.urls import path

from users.views import RegistrationApi,UserLoginApi,LogoutView



urlpatterns = [
    path('RegistrationApi', RegistrationApi.as_view(), name='RegistrationApi'),
    path('UserLoginApi', UserLoginApi.as_view(), name='UserLoginApi'),
    path('LogoutView', LogoutView.as_view(), name='LogoutView'),
   
   
]