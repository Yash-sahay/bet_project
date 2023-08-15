from django.contrib import admin

from users.models import UserProfile,UserBalanceInfo,UserTransactionHistory

class UserBalanceInfoAdmin(admin.ModelAdmin):
    list_display = ['id','user_info', 'current_coins','added_on', 'updated_on' ]


class UserTransactionHistoryAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'credit_coins','debit_coins','net_coins','game_name','added_on']

#Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserBalanceInfo,UserBalanceInfoAdmin)

