from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import ProjectSummaryView


urlpatterns = [
    path('projectsummary/', ProjectSummaryView.as_view(), name='projectSummary-list'),
    path('projectsummary/<int:pk>/', ProjectSummaryView.as_view(), name='projectSummary-detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
