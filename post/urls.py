from django.urls import path
from post.views import blogs, category_blogs, tag_blogs, blog_details



urlpatterns = [
    path('blogs/', blogs, name='blogs'),
    path('category/<str:slug>/', category_blogs, name='category_blogs'),
    path('tag/<str:slug>/', tag_blogs, name='tag_blogs'),
    path('blog/<str:slug>/', blog_details, name='blog_details'),
]