from rest_framework import serializers
from .models import Masterplan

class MasterplanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Masterplan
        fields = ['id', 'project', 'masterplan_name', 'code','image']