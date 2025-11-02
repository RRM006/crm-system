from rest_framework import viewsets, permissions
from .models import Customer
from .serializers import CustomerSerializer


class IsNotCustomerRole(permissions.BasePermission):
	def has_permission(self, request, view):
		# Customers (external) can only read their own info in future; for now block write
		user = request.user
		if not user.is_authenticated:
			return False
		return user.role != getattr(user.Roles, 'CUSTOMER', 'CUSTOMER')


class CustomerViewSet(viewsets.ModelViewSet):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
	permission_classes = [permissions.IsAuthenticated, IsNotCustomerRole]

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user, company=self.request.user.company or '', brand=self.request.user.brand or '')

	def get_queryset(self):
		# Basic multi-tenant filtering by company if set
		qs = super().get_queryset()
		user = self.request.user
		if user.company:
			qs = qs.filter(company=user.company)
		return qs
