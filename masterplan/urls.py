from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import MasterplanView


urlpatterns = [
    path('masterplan/', MasterplanView.as_view(), name='masterplan-list'),
    path('masterplan/<int:pk>/', MasterplanView.as_view(), name='masterplan-detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
