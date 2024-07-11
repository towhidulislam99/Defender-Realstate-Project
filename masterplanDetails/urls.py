from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import MasterplanDetailsView


urlpatterns = [
    path('masterplandetails/', MasterplanDetailsView.as_view(), name='masterplan-details-list'),
    path('masterplandetails/<int:pk>/', MasterplanDetailsView.as_view(), name='masterplan-details-detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
