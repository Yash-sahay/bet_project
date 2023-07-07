from django import views
from django.urls import path

from allusermaster.views import super_agent_register



urlpatterns = [
    path('super_agent_register', super_agent_register.as_view(), name='super_agent_register'),
   
]