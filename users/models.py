from django.db import models
from django.contrib.auth.models import User


# from django.contrib.auth import get_user_model

# # Create your models here.

# User = get_user_model()


# class User(AbstractUser):
#     phone_no = models.CharField(max_length=200, unique=True)
#     otp = models.IntegerField(default=0)
#     is_Verified = models.BooleanField(blank=False, default=False)


class UserAuthTokens(models.Model):
    user_info = models.ForeignKey(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=200,blank=True, null=True)
    refresh_token = models.CharField(max_length=200,blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_auth_tokens'