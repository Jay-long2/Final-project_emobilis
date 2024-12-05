from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(CustomUser)
class ClientsInfo(admin.ModelAdmin):
    model = CustomUser
    list_display = ("username",'password','is_active','date_joined','email',)
    list_filter = ('username','is_active','date_joined')
    search_fields = ('username','email')
    ordering = ('username',)
