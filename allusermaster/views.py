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

                SuperAgentMaster.objects.create(username=username1,super_agent_limit=super_agent_limit,mobile_no=mobile_no,super_agent_share=super_agent_share,match_commission=match_commission,session_commission=session_commission,created_by=usr[0])
                obj=User.objects.create(username=username1,password=make_password(password))
                group = Group.objects.get(name='super_agent')
                obj.groups.add(group)
                return Response({"message":"success"})
            else:
                return Response({"message":"username already exists!"})
        return Response({"message":"something went wrong"})  
     
class getuserlist(APIView):
    def get(self,request,*args,**kwargs):
        obj = SuperAgentMaster.objects.filter().values('id','username')
        return Response({"data":obj})


class GetAllSuperUserAgent(APIView):
    def get(self,request,*args,**kwargs):
        obj = SuperAgentMaster.objects.filter().values('username','mobile_no','super_agent_limit','super_agent_share','match_commission','session_commission')
        return Response({"superagent_list":obj})




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
                 
                AgentMaster.objects.create(username=username1,mobile_no=mobile_no,agent_limit=agent_limit,agent_share=agent_share,match_commission=match_commission,session_commission=session_commission)
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
        obj = AgentMaster.objects.filter().values('id','username')
        return Response({"data":obj})

class allagentlist(APIView):
    def get(self,request,*args,**kwargs):
        agent_list=AgentMaster.objects.filter().values('id','username','super_agent__username','mobile_no','agent_limit','agent_share','match_commission','session_commission')
        return Response({"agent_list":agent_list})

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
                
                ClientMaster.objects.create(username=username1,mobile_no=mobile_no,client_limit=client_limit,match_commission=match_commission,session_commission=session_commission)
                user_obj=User.objects.create(username=username1,password=make_password(password),created_by=usr[0])
                group = Group.objects.get(name='client_master')
                user_obj.groups.add(group)
                return Response({"message":"success"})
            else:
                return Response({"message":"username already exists!"})



class AllClientList(APIView):
    def get(self,request,*args,**kwargs):
        client_list=ClientMaster.objects.filter().values('id','username','agent_master__username','mobile_no','client_limit','match_commission','session_commission')
        return Response({"client_list":client_list})
            
