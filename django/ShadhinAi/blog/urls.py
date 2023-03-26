from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home, projects, blogs, sitemap, login


urlpatterns = [
   
    path("", home , name= 'home'),
    path("projects/", projects , name= 'projects'),
    path("blogs/", blogs , name= 'blogs'),
    path("sitemap/", sitemap , name= 'sitemap'),
    path("login/", login , name= 'login'),
]
