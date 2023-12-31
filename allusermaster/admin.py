from django.contrib import admin
from allusermaster.models import MasterUser, SuperAgentMaster,AgentMaster,ClientMaster
# Register your models here.

class MasterUserAdmin(admin.ModelAdmin):
    list_display= ['id','fullname', 'username','password','mobile_no','master_limit','master_share','match_commission','session_commission','created_by','added_on','updated_on']


class SuperAgentMasterAdmin(admin.ModelAdmin):
    list_display= ['id','fullname', 'username','password','mobile_no','super_agent_limit','super_agent_share','match_commission','session_commission','current_limit','created_by','added_on','updated_on']

class AgentMasterAdmin(admin.ModelAdmin):
    list_display= ['id','fullname', 'username','password', 'mobile_no','agent_limit','agent_share','match_commission','session_commission','created_by','added_on','updated_on']

class ClientMasterAdmin(admin.ModelAdmin):
    list_display= ['id','fullname','username', 'password','mobile_no','client_limit','match_commission','session_commission','created_by','added_on','updated_on']



admin.site.register(MasterUser,MasterUserAdmin)
admin.site.register(SuperAgentMaster,SuperAgentMasterAdmin)
admin.site.register(AgentMaster,AgentMasterAdmin)
admin.site.register(ClientMaster,ClientMasterAdmin)