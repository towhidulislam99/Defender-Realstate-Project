from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404

# API related imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import InvestmentSerializer, InvestmentTwoSerializer, InvestmentThreeSerializer
from .models import Investment, InvestmentTwo, InvestmentThree

import logging

logger = logging.getLogger(__name__)
# Create your views here.

# Investment Model API Class View.
class InvestmentView(APIView):
    
    def get_object(self, pk):
        try:
            return Investment.objects.get(pk=pk)
        except Investment.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            investment_data = self.get_object(pk)
            serializer = InvestmentSerializer(investment_data)
        else:
            investment_data = Investment.objects.all()
            serializer = InvestmentSerializer(investment_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InvestmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        investment_data = self.get_object(pk)
        serializer = InvestmentSerializer(investment_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):  
        investment_data = self.get_object(pk)
        serializer = InvestmentSerializer(investment_data, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        investment_data = self.get_object(pk)
        investment_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#****************************************************************************# 
                        #*****END THIS SECTION*******#
#****************************************************************************# 

# Investment Two Model API Class View.
class InvestmentTwoView(APIView):
    
    def get_object(self, pk):
        try:
            return InvestmentTwo.objects.get(pk=pk)
        except InvestmentTwo.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            investmenttwo_data = self.get_object(pk)
            serializer = InvestmentTwoSerializer(investmenttwo_data)
        else:
            investmenttwo_data = InvestmentTwo.objects.all()
            serializer = InvestmentTwoSerializer(investmenttwo_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InvestmentTwoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        investmenttwo_data = self.get_object(pk)
        serializer = InvestmentTwoSerializer(investmenttwo_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):  
        investmenttwo_data = self.get_object(pk)
        serializer = InvestmentTwoSerializer(investmenttwo_data, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        investmenttwo_data = self.get_object(pk)
        investmenttwo_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#****************************************************************************# 
                        #*****END THIS SECTION*******#
#****************************************************************************# 

# Investment Three Model API Class View.
class InvestmentThreeView(APIView):
    
    def get_object(self, pk):
        try:
            return InvestmentThree.objects.get(pk=pk)
        except InvestmentThree.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            investmentthree_data = self.get_object(pk)
            serializer = InvestmentThreeSerializer(investmentthree_data)
        else:
            investmentthree_data = InvestmentThree.objects.all()
            serializer = InvestmentThreeSerializer(investmentthree_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InvestmentThreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        investmentthree_data = self.get_object(pk)
        serializer = InvestmentThreeSerializer(investmentthree_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):  
        investmentthree_data = self.get_object(pk)
        serializer = InvestmentThreeSerializer(investmentthree_data, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        investmentthree_data = self.get_object(pk)
        investmentthree_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#****************************************************************************# 
                        #*****END THIS SECTION*******#
#****************************************************************************# 
    
# Investment Description Three Model API Class View.
class ManualTestView(APIView):
    
    def get_object(self, pk):
        try:
            return ManualTest.objects.get(pk=pk)
        except ManualTest.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = ManualTestSerializer(data)
        else:
            data = ManualTest.objects.all()
            serializer = ManualTestSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ManualTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = ManualTestSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):  
        data = self.get_object(pk)
        serializer = ManualTestSerializer(data, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#****************************************************************************# 
                        #*****END THIS SECTION*******#
#****************************************************************************# 