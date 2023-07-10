from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import UserAuthTokens
from users.serializers import RegisterSerializer,LoginSerializer
from rest_framework import status, viewsets, mixins
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, renderer_classes, permission_classes
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
            if User.objects.get(username=username):
                return Response({"message":"username must be quinq!"})

            User.objects.create(username=username,password=make_password(password),first_name=first_name,last_name=last_name,email=email)
            return Response({"message":"success"})
        return Response({"message":"somethings went wrong"})


from rest_framework_simplejwt.tokens import RefreshToken
class UserLoginApi(APIView):
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                usr_ob=User.objects.filter(username=username)
                l = usr_ob[0].groups.values_list('name',flat = True)
                refresh = RefreshToken.for_user(usr_ob[0])
              
               
                user_auth_token_obj = UserAuthTokens.objects.filter(
                user_info=usr_ob[0])
                if user_auth_token_obj.exists():
                    user_auth_token_obj.update(
                        access_token=refresh.access_token, refresh_token=refresh)
                    
                else:
                    UserAuthTokens.objects.create(user_info=usr_ob[0], access_token=refresh.access_token,
                                                      refresh_token=refresh)

                return Response({'status': True,"role":l, 'message': 'Log In Successful', 'refresh': str(refresh), 'access': str(refresh.access_token),}, status.HTTP_200_OK)
            else:
                
                return Response({'status': False, 'message': 'Invalid User'}, status.HTTP_200_OK)
        return Response({'status': False, 'message': 'went wrong'}, status.HTTP_200_OK)
    
@permission_classes([IsAuthenticated])    
class LogoutView(APIView) :
    def get(self,request):
        logout(request)
        return Response({'status': True, 'Message': 'Log out successfully'},status.HTTP_200_OK)