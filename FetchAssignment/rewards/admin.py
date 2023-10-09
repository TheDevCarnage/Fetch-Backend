from django.contrib import admin
from .models import Users, Payer
# Register your models here.
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'total_points']

@admin.register(Payer)
class PayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'payer_name', 'points_given', 'paid_to', 'paid_at']
