from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home


urlpatterns = [
    path("", home),
    path("home/", home),
    
]
