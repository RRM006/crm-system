from django.db import models
from django.conf import settings
from customers.models import Customer


class Lead(models.Model):
	class Stage(models.TextChoices):
		NEW = "NEW", "New"
		CONTACTED = "CONTACTED", "Contacted"
		QUALIFIED = "QUALIFIED", "Qualified"
		NEGOTIATION = "NEGOTIATION", "Negotiation"
		WON = "WON", "Closed Won"
		LOST = "LOST", "Closed Lost"

	title = models.CharField(max_length=200)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='leads')
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='leads_owned')
	value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
	stage = models.CharField(max_length=20, choices=Stage.choices, default=Stage.NEW)
	due_date = models.DateField(blank=True, null=True)
	notes = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-updated_at']

	def __str__(self):
		return self.title


class Task(models.Model):
	title = models.CharField(max_length=200)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
	assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='tasks_assigned')
	due_date = models.DateField(blank=True, null=True)
	completed = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
