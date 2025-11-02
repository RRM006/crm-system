from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
	fieldsets = BaseUserAdmin.fieldsets + (
		("CRM Fields", {"fields": ("role", "company", "brand")}),
	)
	list_display = ("username", "email", "role", "is_active", "is_staff", "company", "brand")
	list_filter = ("role", "is_staff", "is_superuser", "is_active", "company", "brand")
	search_fields = ("username", "email", "first_name", "last_name", "company", "brand")

# Register your models here.
