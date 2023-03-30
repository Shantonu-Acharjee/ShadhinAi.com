from django.urls import path
from post.views import blogs



urlpatterns = [
    path('blogs/', blogs, name='blogs')
]