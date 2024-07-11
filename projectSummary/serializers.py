from rest_framework import serializers
from .models import ProjectSummary

class ProjectSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSummary
        fields = ['id', 'icon', 'number', 'title', 'project']