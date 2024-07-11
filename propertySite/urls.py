from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 

urlpatterns = [
    path("", views.indexpage, name='homepage'),
    path("about/", views.aboutpage, name='aboutpage'),
    path("projectdetails/", views.projectDetailspage, name='projectDetailspage'),
    path("investmentpage/", views.investmentpage, name='investmentpage'),
    path("contact/", views.contactpage, name='contactpage'),
    path("manual/", views.manualpage, name='manualpage'),
    # path("404page/", v.errorpage, name='errorpage'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)