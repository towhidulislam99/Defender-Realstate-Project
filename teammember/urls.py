from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import TeamMemberView, AboutUsView, VideoAboutUsView, CeoAboutUsView


urlpatterns = [
    path('aboutus/', AboutUsView.as_view(), name='aboutus-list'),
    path('aboutus/<int:pk>/', AboutUsView.as_view(), name='aboutus-detail'),
    
    path('videoaboutus/', VideoAboutUsView.as_view(), name='videoaboutus-list'),
    path('videoaboutus/<int:pk>/', VideoAboutUsView.as_view(), name='videoaboutus-detail'),
    
    path('ceoaboutus/', CeoAboutUsView.as_view(), name='ceoaboutus-list'),
    path('ceoaboutus/<int:pk>/', CeoAboutUsView.as_view(), name='ceoaboutus-detail'),
    
    path('teammember/', TeamMemberView.as_view(), name='teammember-list'),
    path('teammember/<int:pk>/', TeamMemberView.as_view(), name='teammember-detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
