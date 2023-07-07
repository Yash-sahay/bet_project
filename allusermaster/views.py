from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from allusermaster.serializers import superagentSerializer, agentSerializer
from django.contrib.auth.models import User
from allusermaster.models import SuperAgentMaster,AgentMaster
from rest_framework.response import Response
class super_agent_register(APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        serializer = superagentSerializer(data=data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            mobile_no = serializer.validated_data['mobile_no']
            super_agent_limit = serializer.validated_data['super_agent_limit']
            super_agent_share = serializer.validated_data['super_agent_share']
            match_commission = serializer.validated_data['match_commission']
            session_commission = serializer.validated_data['session_commission']
            
             
            User.objects.create(username=username,password=password)

            SuperAgentMaster.objects.create(username=username,super_agent_limit=super_agent_limit,mobile_no=mobile_no,super_agent_share=super_agent_share,match_commission=match_commission,session_commission=session_commission)
            return Response({"message":"success"})
            
class getuserlist(APIView):
    def get(self,request,*args,**kwargs):
        obj = User.objects.filter().values('id','username')
        return Response({"data":obj})

class agent_register(APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        serializer = agentSerializer(data=data)
        if serializer.is_valid():
            super_agent = serializer.validated_data['super_agent']
            username = serializer.validated_data['username']
            mobile_no = serializer.validated_data['mobile_no']
            password = serializer.validated_data['password']
            agent_limit = serializer.validated_data['agent_limit']
            agent_share= serializer.validated_data['agent_share']
            match_commission = serializer.validated_data['match_commission']
            session_commission = serializer.validated_data['session_commission']
            
            
             
            User.objects.create(username=username,password=password)
            obj=User.objects.filter(username=super_agent)

            AgentMaster.objects.create(super_agent=obj[0],username=username,mobile_no=mobile_no,password=password,agent_limit=agent_limit,agent_share=agent_share,match_commission=match_commission,session_commission=session_commission)
            return Response({"message":"success"})
            