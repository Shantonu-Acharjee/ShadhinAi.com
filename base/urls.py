from django.urls import path
from base.views import home, search_blogs



urlpatterns = [
    path('', home, name='home'),
    path('search_blogs/', search_blogs, name='search_blogs'),
]