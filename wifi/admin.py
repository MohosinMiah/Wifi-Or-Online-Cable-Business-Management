from django.contrib import admin
from .models import Customer
from .models import UserMain
from .models import Payments

# Register your models here.
admin.site.register(Customer)
admin.site.register(UserMain)
# admin.site.register(Payments)

@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    actions = None
    list_display = ("cust_id","pay_amount",)

# @admin.register(Origin)
# class OriginAdmin(admin.ModelAdmin):
#     list_display = ("name",)