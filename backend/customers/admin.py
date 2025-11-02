from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ("first_name", "last_name", "email", "phone", "company", "brand", "updated_at")
	list_filter = ("company", "brand")
	search_fields = ("first_name", "last_name", "email", "phone", "company", "brand")

# Register your models here.
