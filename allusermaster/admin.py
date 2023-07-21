from django.contrib import admin
from allusermaster.models import SuperAgentMaster,AgentMaster,ClientMaster
# Register your models here.

# class SuperAgentMasterAdmin(admin.ModelAdmin):
#     list_display= ['id', 'username', 'mobile_no','super_agent_limit','super_agent_share','match_commission','session_commission','current_limit','added_on','updated_on']

# class AgentMasterAdmin(admin.ModelAdmin):
#     list_display= ['id','super_agent', 'username', 'mobile_no','agent_limit','agent_share','match_commission','session_commission','added_on','updated_on']

# class ClientMasterAdmin(admin.ModelAdmin):
#     list_display= ['id','agent_master', 'username', 'mobile_no','client_limit','match_commission','session_commission','added_on','updated_on']




admin.site.register(SuperAgentMaster)
admin.site.register(AgentMaster)
admin.site.register(ClientMaster)