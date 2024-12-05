from django.contrib import admin
from .models import Client
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(Client)
class ClientsInfo(admin.ModelAdmin):
    model = Client
    list_display = ("name",'phone','message')
    list_filter = ('name','phone')
    search_fields = ('name','email')
    ordering = ('name',)
