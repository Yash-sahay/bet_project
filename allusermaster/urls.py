from django import views
from django.urls import path

from allusermaster.views import super_agent_register,agent_register,getuserlist,agentuserlist,clientmaster_register,GetAllSuperUserAgent,allagentlist,AllClientList,UpdateUserLimit,UserbassedAllClientList,UserbassedSuperAgentMaster,UserbassedAgentMaster,UserDashbordApi
                        



urlpatterns = [
    path('super_agent_register', super_agent_register.as_view(), name='super_agent_register'),
    path('agent_register', agent_register.as_view(), name='agent_register'),
    path('getuserlist', getuserlist.as_view(), name='getuserlist'),
    path('agentuserlist', agentuserlist.as_view(), name='agentuserlist'),
    path('clientmaster_register', clientmaster_register.as_view(), name='clientmaster_register'),
    path('GetAllSuperUserAgent', GetAllSuperUserAgent.as_view(), name='GetAllSuperUserAgent'),
    path('allagentlist', allagentlist.as_view(), name='allagentlist'),
    path('AllClientList',AllClientList.as_view(), name='AllClientList'),
    path('UpdateUserLimit/<int:id>',UpdateUserLimit.as_view(), name='UpdateUserLimit'),
    path('UserbassedAllClientList',UserbassedAllClientList.as_view(),name='UserbassedAllClientList'),
    path('UserbassedSuperAgentMaster',UserbassedSuperAgentMaster.as_view(),name='UserbassedSuperAgentMaster'),
    path('UserbassedAgentMaster',UserbassedAgentMaster.as_view(),name='UserbassedAgentMaster'),
    path('userDashbordApi',UserDashbordApi.as_view(),name="userDashbordApi")
   
]