from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import ClientReviewView


urlpatterns = [
    path('clientreview/', ClientReviewView.as_view(), name='clientReview-list'),
    path('clientreview/<int:pk>/', ClientReviewView.as_view(), name='clientReview-detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
