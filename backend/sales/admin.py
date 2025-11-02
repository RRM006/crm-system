from django.contrib import admin
from .models import Lead, Task


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
	list_display = ("title", "customer", "owner", "value", "stage", "updated_at")
	list_filter = ("stage",)
	search_fields = ("title", "customer__first_name", "customer__last_name", "owner__username")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ("title", "customer", "assignee", "due_date", "completed", "updated_at")
	list_filter = ("completed",)
	search_fields = ("title", "customer__first_name", "customer__last_name", "assignee__username")

# Register your models here.
