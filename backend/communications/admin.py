from django.contrib import admin
from .models import Complaint


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
	list_display = ("title", "customer", "status", "created_by", "assignee", "updated_at")
	list_filter = ("status",)
	search_fields = ("title", "customer__first_name", "customer__last_name", "created_by__username")

# Register your models here.
