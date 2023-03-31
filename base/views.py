from django.shortcuts import render
from post.models import Blog


def home(request):
    blogs = Blog.objects.order_by('-created_date')
    context = {
        'blogs' : blogs
    }
    return render(request, 'home/home.html', context)
