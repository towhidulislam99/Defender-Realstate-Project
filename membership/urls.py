from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import MembershipView


urlpatterns = [
    path('membership/', MembershipView.as_view(), name='membership-list'),
    path('membership/<int:pk>/', MembershipView.as_view(), name='membership-detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
