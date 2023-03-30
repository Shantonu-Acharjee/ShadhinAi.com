from django.shortcuts import render
from .models import Blog

def blogs(request):
    blogs = Blog.objects.order_by('-created_date')
    context = {
        'blogs' : blogs
    }
    return render(request, 'blogs/blogs.html', context)
