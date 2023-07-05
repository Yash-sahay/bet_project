from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
# from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    username = serializers.CharField()
    first_name = serializers.CharField(default='')
    last_name = serializers.CharField(default='')
    email=serializers.EmailField(default='')

    # first_name = serializers.CharField(max_length=10)

    # def create(self, validated_data):
    #     user = User.objects.create_user(validated_data['username'],
    #                                     validated_data['password'])
    #     user.email = validated_data['email']
    #     user.first_name = validated_data['first_name']
    #     user.last_name = validated_data['last_name']
    #     user.save()
    #     return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')