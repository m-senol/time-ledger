from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_manager', 'hire_date', 'available_leave_days')
    list_filter = ('is_manager',)