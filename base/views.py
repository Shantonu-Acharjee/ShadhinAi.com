from django.shortcuts import render, redirect
from post.models import Blog
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from . models import Slider
from django.db.models import Q


def home(request):
    queryset = Blog.objects.order_by('-created_date')
    sliders = Slider.objects.order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 12)# enter how many post you want to see on single page

    try:
        blogs = paginator.page(page)

    except EmptyPage:
        blogs = paginator.page(1)

    except PageNotAnInteger:
        blogs = paginator.page(1)
        return redirect('home')

    context = {
        'blogs': blogs,
        'paginator': paginator,
        'sliders': sliders,
    }

    return render(request, 'home/home.html', context)


def search_blogs(request):

    search_key = request.GET.get('q', None)

    if search_key:

        blogs = Blog.objects.filter(

            Q(title__icontains = search_key) |
            Q(category__title__icontains = search_key) |
            Q(user__username__icontains = search_key) |
            Q(tags__title__icontains = search_key)

        ).distinct()

        context ={
            "blogs" : blogs
        }

        
    

    else:
        blogs = Blog.objects.order_by('-created_date')

        context ={
            "blogs" : blogs
        }



    return render(request, 'base/search.html', context)
