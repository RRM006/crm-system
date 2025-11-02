from rest_framework import viewsets, permissions
from .models import Complaint
from .serializers import ComplaintSerializer


class ComplaintViewSet(viewsets.ModelViewSet):
	queryset = Complaint.objects.select_related('customer', 'created_by', 'assignee').all()
	serializer_class = ComplaintSerializer
	permission_classes = [permissions.IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)
