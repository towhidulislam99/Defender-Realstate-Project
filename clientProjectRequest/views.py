from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404

# API related imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClientProjectRequestSerializer
from .models import ClientProjectRequest

import logging

logger = logging.getLogger(__name__)
# Create your views here.


# Contact Info Model API Class View.
class ClientProjectRequestView(APIView):
    
    def get_object(self, pk):
        try:
            return ClientProjectRequest.objects.get(pk=pk)
        except ClientProjectRequest.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            client_data = self.get_object(pk)
            serializer = ClientProjectRequest(client_data)
        else:
            client_data = ClientProjectRequest.objects.all()
            serializer = ClientProjectRequestSerializer(client_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClientProjectRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        contact_data = self.get_object(pk)
        serializer = ClientProjectRequestSerializer(contact_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        client_data = self.get_object(pk)
        serializer = ClientProjectRequestSerializer(client_data, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        client_data = self.get_object(pk)
        client_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#****************************************************************************# 
                        #*****END THIS SECTION*******#
#****************************************************************************# 


# Contact Info Model API Class View.
class UserContactView(APIView):
    
    def get_object(self, pk):
        try:
            return UserContact.objects.get(pk=pk)
        except UserContact.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            user_data = self.get_object(pk)
            serializer = UserContactSerializer(user_data)
        else:
            user_data = UserContact.objects.all()  # Corrected from ContactInfo to UserContact
            serializer = UserContactSerializer(user_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        user_data = self.get_object(pk)
        serializer = UserContactSerializer(user_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):  # Added patch method
        user_data = self.get_object(pk)
        serializer = UserContactSerializer(user_data, data=request.data, partial=True)  # partial=True allows partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_data = self.get_object(pk)
        user_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#****************************************************************************# 
                        #*****END THIS SECTION*******#
#****************************************************************************# 