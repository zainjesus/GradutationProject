from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    """Профиль пользователя"""
    list_display = ("user", "first_name", "last_name", "phone", "email")
    search_fields = ("user", "first_name", "last_name", "phone", "email")

