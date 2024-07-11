from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404

# API related imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProjectSummarySerializer
from .models import ProjectSummary

import logging

logger = logging.getLogger(__name__)
# Create your views here.


# Company Summary Model API Class View.
class ProjectSummaryView(APIView):
    
    def get_object(self, pk):
        try:
            return ProjectSummary.objects.get(pk=pk)
        except ProjectSummary.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            psummary_data = self.get_object(pk)
            serializer = ProjectSummarySerializer(psummary_data)
        else:
            psummary_data = ProjectSummary.objects.all()
            serializer = ProjectSummarySerializer(psummary_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectSummarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        psummary_data = self.get_object(pk)
        serializer = ProjectSummarySerializer(psummary_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):  
        psummary_data = self.get_object(pk)
        serializer = ProjectSummarySerializer(psummary_data, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        psummary_data = self.get_object(pk)
        psummary_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#****************************************************************************# 
                        #*****END THIS SECTION*******#
#****************************************************************************# 