from django import views
from django.urls import path

from allusermaster.views import GetAllUserCount, UpdateAgentDetail, UpdateClientDetail, UpdateMasterUser, UpdateSuperAgent, UserTransactionHistoryApi, getallmasteruserforlist, master_register, super_agent_register,agent_register,getuserlist,agentuserlist,clientmaster_register,GetAllSuperUserAgent,allagentlist,AllClientList,UpdateUserLimit,UserbassedAllClientList,UserbassedSuperAgentMaster,UserbassedAgentMaster,UserDashbordApi,GetMasterUser
                        



urlpatterns = [
    path('master_register', master_register.as_view(), name='master_register'),
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
    path('userDashbordApi',UserDashbordApi.as_view(),name="userDashbordApi"),
    path('user_Transaction_history',UserTransactionHistoryApi.as_view(),name='user_Transaction_history'),
    path('GetMasterUser',GetMasterUser.as_view(),name='GetMasterUser'),
    path('GetAllUserCount',GetAllUserCount.as_view(),name='GetAllUserCount'),

    path('UpdateMasterUser/<int:id>',UpdateMasterUser.as_view(),name='UpdateMasterUser'),
    path('UpdateSuperAgent/<int:id>',UpdateSuperAgent.as_view(),name='UpdateSuperAgent'),
    path('UpdateAgentDetail/<int:id>',UpdateAgentDetail.as_view(),name='UpdateAgentDetail'),
    path('UpdateClientDetail/<int:id>',UpdateClientDetail.as_view(),name='UpdateClientDetail'),
    path('getallmasteruserforlist',getallmasteruserforlist.as_view(),name='getallmasteruserforlist'),


   
]