from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	class Roles(models.TextChoices):
		ADMIN = "ADMIN", "Admin"
		SALES = "SALES", "Sales Executive"
		SUPPORT = "SUPPORT", "Customer Support Agent"
		MANAGER = "MANAGER", "Manager/Supervisor"
		CUSTOMER = "CUSTOMER", "Customer"

	# Username remains for admin compatibility; email will be unique for login in APIs
	email = models.EmailField(unique=True)
	role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.CUSTOMER)
	company = models.CharField(max_length=100, blank=True, null=True, help_text="Optional company/tenant tag")
	brand = models.CharField(max_length=100, blank=True, null=True, help_text="Optional brand tag")

	REQUIRED_FIELDS = ["email"]

	def __str__(self):
		name = self.get_full_name() or self.username or self.email
		return f"{name} ({self.role})"
