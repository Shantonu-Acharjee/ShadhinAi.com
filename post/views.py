from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Tag, Category, Comment, Reply
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from .forms import TextForm
from django.contrib.auth.decorators import login_required


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




def blog_details(request, slug):
    form = TextForm()
    blog = get_object_or_404(Blog, slug=slug)
    category = Category.objects.get(id = blog.category.id)
    related_blogs = category.category_blogs.all()

    if request.method == "POST" and request.user.is_authenticated:
        form = TextForm(request.POST)

        if form.is_valid():

            Comment.objects.create(
                user=request.user,
                blog=blog,
                text=form.cleaned_data.get('text')
            )

            return redirect('blog_details', slug=slug)


    context = {
        "blog": blog,
        "related_blogs" : related_blogs,
        "form": form,
    }

    return render(request, 'blogs/blog_details.html', context)



@login_required(login_url='login')
def add_reply(request, blog_id, comment_id):
    
    blog = get_object_or_404(Blog, id = blog_id)

    if request.method == 'POST':
        form = TextForm(request.POST)

        if form.is_valid():
            
            comment = get_object_or_404(Comment, id =comment_id)
            Reply.objects.create(
                user = request.user,
                comment = comment,
                text = form.cleaned_data.get('text')
            )

    return redirect('blog_details', slug = blog.slug)

 
 





