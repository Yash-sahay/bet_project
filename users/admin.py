from django.contrib import admin

from users.models import UserProfile,UserBalanceInfo,UserTransactionHistory



#Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserBalanceInfo)
admin.site.register(UserTransactionHistory)

