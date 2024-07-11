from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404

# API related imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import MasterplanSerializer
from .models import Masterplan

import logging

logger = logging.getLogger(__name__)
# Create your views here.


# Master Plan Model API Class View.
class MasterplanView(APIView):
    
    def get_object(self, pk):
        try:
            return Masterplan.objects.get(pk=pk)
        except Masterplan.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            masterplan_data = self.get_object(pk)
            serializer = MasterplanSerializer(masterplan_data)
        else:
            masterplan_data = Masterplan.objects.all()
            serializer = MasterplanSerializer(masterplan_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MasterplanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        masterplan_data = self.get_object(pk)
        serializer = MasterplanSerializer(masterplan_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):  
        masterplan_data = self.get_object(pk)
        serializer = MasterplanSerializer(masterplan_data, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        masterplan_data = self.get_object(pk)
        masterplan_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#****************************************************************************# 
                        #*****END THIS SECTION*******#
#****************************************************************************# 