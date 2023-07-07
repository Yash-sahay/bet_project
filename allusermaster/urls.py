from django import views
from django.urls import path

from allusermaster.views import super_agent_register,agent_register,getuserlist



urlpatterns = [
    path('super_agent_register', super_agent_register.as_view(), name='super_agent_register'),
    path('agent_register', agent_register.as_view(), name='agent_register'),
    path('getuserlist', getuserlist.as_view(), name='getuserlist'),
   
]