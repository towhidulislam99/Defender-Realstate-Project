from rest_framework import serializers
from .models import ClientReview

class ClientReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientReview
        fields = ['id', 'name', 'description', 'image']