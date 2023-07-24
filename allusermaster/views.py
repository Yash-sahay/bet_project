from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from allusermaster.serializers import superagentSerializer, agentSerializer,clientSerializer,updateuserSerializer
from django.contrib.auth.models import User,Group
from allusermaster.models import SuperAgentMaster,AgentMaster,ClientMaster
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, renderer_classes, permission_classes

from allusermaster.utility import role_validations


@permission_classes([IsAuthenticated]) 
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
            
            
            usr=request.user.username
            usr=User.objects.filter(username=usr)
            sucount=SuperAgentMaster.objects.filter(created_by__id=usr[0].id).count()
            sucount+1
            username1='SA'+ str(sucount+1)+username
            print(username1)
            obj = User.objects.filter(username=username1)

            if not obj.exists():

                SuperAgentMaster.objects.create(username=username1,password=password,super_agent_limit=super_agent_limit,mobile_no=mobile_no,super_agent_share=super_agent_share,match_commission=match_commission,session_commission=session_commission,created_by=usr[0])
                obj=User.objects.create(username=username1,password=make_password(password))
                group = Group.objects.get(name='super_agent')
                obj.groups.add(group)
                return Response({"message":"success"})
            else:
                return Response({"message":"username already exists!"})
        return Response({"message":"something went wrong"})  
     
class getuserlist(APIView):
    def get(self,request,*args,**kwargs):
        obj = SuperAgentMaster.objects.values('id','username')
        return Response({"data":obj})



class UpdateUserLimit(APIView):
    def put(self,request,id,*args,**kwargs):
        data = request.data
        serializer = updateuserSerializer(data=data)
        if serializer.is_valid():
            
            current_limit = serializer.validated_data['current_limit']

            obj = SuperAgentMaster.objects.filter(id=id)
            obj1 =  obj.filter(id=id).values('super_agent_limit')
           
            jjjj = int(obj1[0]["super_agent_limit"])
            
            if jjjj < int(current_limit):

                obj.update(super_agent_limit=current_limit,current_limit=current_limit)
            else:
                obj.update(current_limit=current_limit)

            return Response({"message":"success"})



@permission_classes([IsAuthenticated])
class agent_register(APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        serializer = agentSerializer(data=data)
        if serializer.is_valid():
            
            username = serializer.validated_data['username']
            mobile_no = serializer.validated_data['mobile_no']
            password = serializer.validated_data['password']
            agent_limit = serializer.validated_data['agent_limit']
            agent_share= serializer.validated_data['agent_share']
            match_commission = serializer.validated_data['match_commission']
            session_commission = serializer.validated_data['session_commission']
            

            usr=request.user.username
            usr=User.objects.filter(username=usr)
            sucount=AgentMaster.objects.filter(created_by__id=usr[0].id).count()
            sucount+1
            username1='A'+ str(sucount+1)+username
            print(username1)
            obj = User.objects.filter(username=username1)
            
            if not obj.exists():
                 
                AgentMaster.objects.create(username=username1,password=password,mobile_no=mobile_no,agent_limit=agent_limit,agent_share=agent_share,match_commission=match_commission,session_commission=session_commission)
                user_obj=User.objects.create(username=username1,password=make_password(password),created_by=usr[0])
                group = Group.objects.get(name='agent_master')
                user_obj.groups.add(group)
                return Response({"message":"success"})
            else:
                return Response({"message":"username already exists!"})
        else:
            return Response({"message":"data is not valid!"})


class agentuserlist(APIView):
    def get(self,request,*args,**kwargs):
        obj = AgentMaster.objects.values('id','username')
        return Response({"data":obj})

@permission_classes([IsAuthenticated])
class clientmaster_register(APIView):
    def post(self,request,*args,**kwargs):
        data=request.data
        serializer = clientSerializer(data=data)
        if serializer.is_valid():
            
            username = serializer.validated_data['username']
            mobile_no = serializer.validated_data['mobile_no']
            password = serializer.validated_data['password']
            client_limit = serializer.validated_data['client_limit']
            match_commission = serializer.validated_data['match_commission']
            session_commission = serializer.validated_data['session_commission']
            
            
            usr=request.user.username
            usr=User.objects.filter(username=usr)
            sucount=AgentMaster.objects.filter(created_by__id=usr[0].id).count()
            sucount+1
            username1='A'+ str(sucount+1)+username
            print(username1)
            obj = User.objects.filter(username=username1)
            
            if not obj.exists():
                
                ClientMaster.objects.create(username=username1,password=password,mobile_no=mobile_no,client_limit=client_limit,match_commission=match_commission,session_commission=session_commission)
                user_obj=User.objects.create(username=username1,password=make_password(password),created_by=usr[0])
                group = Group.objects.get(name='client_master')
                user_obj.groups.add(group)
                return Response({"message":"success"})
            else:
                return Response({"message":"username already exists!"})


@permission_classes([IsAuthenticated])
class AllClientList(APIView):
    def get(self,request,*args,**kwargs):
        usr = request.user.username
        usr_ob = User.objects.filter(username=usr)
        if usr_ob[0].groups.filter(name='super_agent').exists():
            client_list=ClientMaster.objects.values('id','username','password','mobile_no','client_limit','match_commission','session_commission','created_by__username')
            return Response({"client_list":client_list})
        else:
            usr=request.user.id
            client_list=ClientMaster.objects.filter(created_by=usr).values('id','username','password','mobile_no','client_limit','match_commission','session_commission','created_by__username')
            return Response({"client_list":client_list})
        




#user bassed code here==============================================================

@permission_classes([IsAuthenticated]) 
class UserbassedAllClientList(APIView):
    def get(self,request,*args,**kwargs):
        usr=request.user.id
        client_list=ClientMaster.objects.filter(created_by=usr).values('id','username','password','mobile_no','client_limit','match_commission','session_commission','created_by__username')
        return Response({"client_list":client_list})
    


@permission_classes([IsAuthenticated]) 
class UserbassedSuperAgentMaster(APIView):
    def get(self,request,*args,**kwargs):
        usr=request.user.id
        obj = SuperAgentMaster.objects.filter(created_by=usr).values('username','password','mobile_no','super_agent_limit','super_agent_share','match_commission','session_commission','created_by__username')
        return Response({"superagent_list":obj})

@permission_classes([IsAuthenticated]) 
class UserbassedAgentMaster(APIView):
    def get(self,request,*args,**kwargs):
        usr=request.user.id
        agent_list=AgentMaster.objects.filter(created_by=usr).values('id','username','password','mobile_no','agent_limit','agent_share','match_commission','session_commission','created_by__username')
        return Response({"agent_list":agent_list})


from django.utils.decorators import method_decorator
@permission_classes([IsAuthenticated])
class GetAllSuperUserAgent(APIView):
    def get(self,request,*args,**kwargs):
        usr = request.user.username
        usr_ob = User.objects.filter(username=usr)
        if usr_ob[0].groups.filter(name='super_agent').exists():
            obj = SuperAgentMaster.objects.values('username','password','mobile_no','super_agent_limit','super_agent_share','match_commission','session_commission','created_by__username')
            return Response({"superagent_list":obj})
        else:
             usr=request.user.id
             obj = SuperAgentMaster.objects.filter(created_by=usr).values('username','password','mobile_no','super_agent_limit','super_agent_share','match_commission','session_commission','created_by__username')
             return Response({"superagent_list":obj})
    
@permission_classes([IsAuthenticated])
class allagentlist(APIView):
    def get(self,request,*args,**kwargs):
        usr = request.user.username
        usr_ob = User.objects.filter(username=usr)
        if usr_ob[0].groups.filter(name='super_agent').exists():
            agent_list=AgentMaster.objects.values('id','username','password','mobile_no','agent_limit','agent_share','match_commission','session_commission','created_by__username')
            return Response({"agent_list":agent_list})
        else:
             usr=request.user.id
             agent_list=AgentMaster.objects.filter(created_by=usr).values('id','username','password','mobile_no','agent_limit','agent_share','match_commission','session_commission','created_by__username')
             return Response({"agent_list":agent_list})