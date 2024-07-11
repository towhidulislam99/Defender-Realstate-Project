from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import ContactInfoView, UserContactView, ContactUsView


urlpatterns = [
    path('contactinfo/', ContactInfoView.as_view(), name='contactinfo-list'),
    path('contactinfo/<int:pk>/', ContactInfoView.as_view(), name='contactinfo-detail'),
    
    path('usercontact/', UserContactView.as_view(), name='usercontact-list'),
    path('usercontact/<int:pk>/', UserContactView.as_view(), name='usercontact-detail'),
    
    path('contactus/', ContactUsView.as_view(), name='contactus-list'),
    path('contactus/<int:pk>/', ContactUsView.as_view(), name='contactus-detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
