from django.db import models
from django.contrib.auth.models import User


# from django.contrib.auth import get_user_model

# # Create your models here.

# User = get_user_model()


# class User(AbstractUser):
#     phone_no = models.CharField(max_length=200, unique=True)
#     otp = models.IntegerField(default=0)
#     is_Verified = models.BooleanField(blank=False, default=False)

class UserProfile(models.Model):
	user_info = models.OneToOneField(User,on_delete = models.CASCADE)
	mob=models.CharField(max_length=15,blank=True,null=True)
	created_by=models.ForeignKey(User,on_delete=models.CASCADE, related_name = 'user_profile')
	added_on = models.DateTimeField(auto_now_add = True)
	updated_on = models.DateTimeField(auto_now = True)

	class Meta:
		db_table = 'user_profile_info'




class UserAuthTokens(models.Model):
    user_info = models.ForeignKey(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=800,blank=True, null=True)
    refresh_token = models.CharField(max_length=800,blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_auth_tokens'

class UserBalanceInfo(models.Model):
	user_info = models.OneToOneField(User,on_delete = models.CASCADE)
	current_coins = models.IntegerField(default = 0)
	added_on = models.DateTimeField(auto_now_add = True)
	updated_on = models.DateTimeField(auto_now = True)

	class Meta:
		db_table = 'user_balance_info'
                
class UserTransactionHistory(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'user_transactions')
	credit_coins = models.FloatField(default = 0)
	debit_coins = models.FloatField(default = 0)
	net_coins = models.FloatField(default = 0)
	game_name = models.CharField(max_length = 100,blank = True,null = True)
	added_on = models.DateTimeField(auto_now_add = True)
	
	class Meta:
		db_table = 'user_transaction_history'
