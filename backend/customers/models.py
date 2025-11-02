from django.db import models
from django.conf import settings


class Customer(models.Model):
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='customers_created')
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100, blank=True)
	email = models.EmailField(blank=True, null=True)
	phone = models.CharField(max_length=50, blank=True)
	address = models.TextField(blank=True)
	notes = models.TextField(blank=True)
	company = models.CharField(max_length=100, blank=True, help_text='Tenant/company segregation key')
	brand = models.CharField(max_length=100, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-updated_at']

	def __str__(self):
		return f"{self.first_name} {self.last_name}".strip()
