from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.


class super_agent_register(APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        serializer = superagentSerializer(data=data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            super_agent_limit = serializer.validated_data['super_agent_limit']
            super_agent_share = serializer.validated_data['super_agent_share']
            match_commission = serializer.validated_data['match_commission']
            session_commission = serializer.validated_data['session_commission']

            User.objects.create(username=username,password=password)

            SuperAgentMaster.objects.create(super_agent_limit=super_agent_limit,super_agent_share=super_agent_share,match_commission=match_commission,)
            return Response({"message":"success"})
            