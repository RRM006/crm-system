from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Lead, Task
from .serializers import LeadSerializer, TaskSerializer


class LeadViewSet(viewsets.ModelViewSet):
	queryset = Lead.objects.select_related('customer', 'owner').all()
	serializer_class = LeadSerializer
	permission_classes = [permissions.IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.select_related('customer', 'assignee').all()
	serializer_class = TaskSerializer
	permission_classes = [permissions.IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(assignee=self.request.user)
