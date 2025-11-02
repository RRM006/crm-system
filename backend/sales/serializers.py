from rest_framework import serializers
from .models import Lead, Task


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id', 'title', 'customer', 'owner', 'value', 'stage', 'due_date', 'notes', 'created_at', 'updated_at']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'customer', 'assignee', 'due_date', 'completed', 'created_at', 'updated_at']
        read_only_fields = ['id', 'assignee', 'created_at', 'updated_at']
