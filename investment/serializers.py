from rest_framework import serializers
from .models import Investment, InvestmentTwo, InvestmentThree

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = ['id','title', 'image', 'description']
        


class InvestmentTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentTwo
        fields = ['id','title', 'image', 'description']
        


        

class InvestmentThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentThree
        fields = ['id','title', 'image', 'description']
        


