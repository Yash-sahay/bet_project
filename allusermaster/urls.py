from django import views
from django.urls import path

from allusermaster.views import super_agent_register,agent_register,getuserlist,agentuserlist,clientmaster_register



urlpatterns = [
    path('super_agent_register', super_agent_register.as_view(), name='super_agent_register'),
    path('agent_register', agent_register.as_view(), name='agent_register'),
    path('getuserlist', getuserlist.as_view(), name='getuserlist'),
    path('agentuserlist', agentuserlist.as_view(), name='agentuserlist'),
    path('clientmaster_register', clientmaster_register.as_view(), name='clientmaster_register'),
   
]