from django.shortcuts import render, redirect
from post.models import Blog
from django.core.paginator import PageNotAnInteger, EmptyPage,Paginator


def home(request):
    queryset = Blog.objects.order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 1) #enter how many post you want to see on single page

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
    }

    return render(request, 'home/home.html', context)
