from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home, projects


urlpatterns = [
   
    path("", home , name= 'home'),
    path("projects/", projects , name= 'projects'),
    
]
