from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import CompanySummaryView


urlpatterns = [
    path('companysummary/', CompanySummaryView.as_view(), name='compantSummary-list'),
    path('companysummary/<int:pk>/', CompanySummaryView.as_view(), name='companySummary-detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
