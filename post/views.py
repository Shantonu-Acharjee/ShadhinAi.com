from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Tag, Category
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator


def blogs(request):

    queryset = Blog.objects.order_by('-created_date')
    page = request.GET.get('page', 1)
    # enter how many post you want to see on single page
    paginator = Paginator(queryset, 18)

    try:
        blogs = paginator.page(page)

    except EmptyPage:
        blogs = paginator.page(1)

    except PageNotAnInteger:
            blogs = paginator.page(1)
            return redirect('blogs')

    context = {
        'blogs': blogs,
        'paginator': paginator,
    }
    return render(request, 'blogs/blogs.html', context)







def category_blogs(request, slug):
    category = get_object_or_404(Category, slug=slug)
    queryset = category.category_blogs.all()

    
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 2)
    
    
    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
        blogs = paginator.page(1)
        return redirect('blogs')

    context = {
        "blogs": blogs,
        "category_name" : category,
    }
     
    return render(request, 'blogs/category_blogs.html', context)






def tag_blogs(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    queryset = tag.tag_blogs.all()

    
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 2)
    
    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
        blogs = paginator.page(1)
        return redirect('blogs')

    context = {
        "blogs": blogs,
        "category_name" : tag,
    }
     
    return render(request, 'blogs/category_blogs.html', context)
 
 