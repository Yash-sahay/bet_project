from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import UserAuthTokens
from users.serializers import RegisterSerializer
from rest_framework import status, viewsets, mixins
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.

# class RegistrationApi(APIView):
#     def post(self,request):
#         serializer = RegisterSerializer(data=request.data)
        
#         if serializer.is_valid():
           
#             serializer.save()
#         else:
            
#             return Response({'status': False, 'message': 'Invalid Details'}, status.HTTP_403_FORBIDDEN)
#         logging.info('Now Checking User Details except Username, email and password')
#         user_serializer = UserSerializer(data=request.data)
#         if user_serializer.is_valid():
#             logging.info('User Details Are Valid')
#             user_serializer.save()
#             logging.info('User Details are Valid And Saved Successfully')
#         else:
#             logging.error('User Details Are Invalid and the error says - ' + str(user_serializer.errors))
#             return Response({'status': False, 'message': 'Invalid Files'}, status.HTTP_404_NOT_FOUND)
#         data = serializer.data
#         data.update(user_serializer.data)
#         return Response({'status': True, 'data': data}, status.HTTP_201_CREATED)

class RegistrationApi(APIView):
    def post(self,request,*args,**kwargs):

        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            first_name = serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']
            email = serializer.validated_data['email']

            User.objects.create(username=username,password=make_password(password),first_name=first_name,last_name=last_name,email=email)
            return Response({"message":"success"})



class UserLoginApi(APIView):
    def post(self,request):
        pass