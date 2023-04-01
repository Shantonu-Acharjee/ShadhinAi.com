from django.shortcuts import render, redirect
from post.models import Blog
from django.core.paginator import PageNotAnInteger, EmptyPage,Paginator
from . models import Slider


def home(request):
    queryset = Blog.objects.order_by('-created_date')
    sliders = Slider.objects.order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 2) #enter how many post you want to see on single page

    try:
        blogs = paginator.page(page)

    except EmptyPage:
        blogs = paginator.page(1)

    except PageNotAnInteger:
            blogs = paginator.page(1)
            return redirect('home')

    context = {
        'blogs' : blogs,
        'paginator' : paginator,
        'sliders' : sliders,
    }

    return render(request, 'home/home.html', context)
