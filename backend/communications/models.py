from django.db import models
from django.conf import settings
from customers.models import Customer


class Complaint(models.Model):
	STATUS_CHOICES = (
		("OPEN", "Open"),
		("IN_PROGRESS", "In Progress"),
		("RESOLVED", "Resolved"),
		("CLOSED", "Closed"),
	)

	title = models.CharField(max_length=200)
	description = models.TextField()
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="complaints")
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="complaints_created")
	assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="complaints_assigned")
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="OPEN")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.title} ({self.status})"
