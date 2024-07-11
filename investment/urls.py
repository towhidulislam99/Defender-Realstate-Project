from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import InvestmentView,InvestmentTwoView, InvestmentThreeView


urlpatterns = [
    path('investment/', InvestmentView.as_view(), name='investment-list'),
    path('investment/<int:pk>/', InvestmentView.as_view(), name='investment-detail'),
    
    
    path('investmenttwo/', InvestmentTwoView.as_view(), name='investmenttwo-list'),
    path('investmenttwo/<int:pk>/', InvestmentTwoView.as_view(), name='investmenttwo-detail'),
    
   
    path('investmentthree/', InvestmentThreeView.as_view(), name='investmentthree-list'),
    path('investmentthree/<int:pk>/', InvestmentThreeView.as_view(), name='investmentthree-detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
