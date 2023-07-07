from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class SuperAgentMaster(models.Model):
   username = models.ForeignKey(User, on_delete=models.CASCADE)
   mobile_no = models.CharField(max_length=10,blank=True,null=True)
   super_agent_limit = models.CharField(max_length=20)
   super_agent_share = models.CharField(max_length=20)
   match_commission = models.CharField(max_length=20)
   session_commission = models.CharField(max_length=20)
   added_on = models.DateTimeField(auto_now_add=True)
   updated_on = models.DateTimeField(auto_now=True)


class AgentMaster(models.Model):
   super_agent = models.ForeignKey(SuperAgentMaster,on_delete=models.CASCADE)
   username = models.ForeignKey(User, on_delete=models.CASCADE)
   mobile_no = models.CharField(max_length=20,blank=True,null=True)
   agent_limit = models.CharField(max_length=20)
   agent_share = models.CharField(max_length=20)
   match_commission = models.CharField(max_length=20)
   session_commission = models.CharField(max_length=20)
   added_on = models.DateTimeField(auto_now_add=True)
   updated_on = models.DateTimeField(auto_now=True)



class ClientMaster(models.Model):
   agent_master = models.ForeignKey(AgentMaster,on_delete=models.CASCADE)
   username = models.ForeignKey(User, on_delete=models.CASCADE)
   mobile_no = models.CharField(max_length=10,blank=True,null=True)
   client_limit = models.CharField(max_length=20)
   match_commission = models.CharField(max_length=20)
   session_commission = models.CharField(max_length=20)
   added_on = models.DateTimeField(auto_now_add=True)
   updated_on = models.DateTimeField(auto_now=True)
