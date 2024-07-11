from rest_framework import serializers
from .models import ClientProjectRequest

class ClientProjectRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProjectRequest
        fields = ['id', 'project', 'name', 'email', 'comment']