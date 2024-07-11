from rest_framework import serializers
from .models import CompanySummary

class CompanySummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanySummary
        fields = ['id', 'title', 'amount', 'icon']