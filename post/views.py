from django.shortcuts import render, redirect
from .models import Blog
from django.core.paginator import PageNotAnInteger, EmptyPage,Paginator


def blogs(request):

    queryset = Blog.objects.order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 18) #enter how many post you want to see on single page

    try:
        blogs = paginator.page(page)

    except EmptyPage:
        blogs = paginator.page(1)

    except PageNotAnInteger:
            blogs = paginator.page(1)
            return redirect('blogs')


    context = {
        'blogs' : blogs,
        'paginator' : paginator,
    }
    return render(request, 'blogs/blogs.html', context)
 