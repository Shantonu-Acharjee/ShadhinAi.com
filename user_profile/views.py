from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, LoginForm, UserProfileUpdateForm, ProfilePictureUpdateForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .decorators import not_logged_in_required
from post.models import Blog, Category, Tag
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.contrib.auth.decorators import login_required
from .models import User, Follow
from post.forms import AddBlogForm
from django.utils.text import slugify

@not_logged_in_required
def login_user(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data.get('username'),
                password = form.cleaned_data.get('password')
            )

            if user:
                login(request, user)
                return redirect('home')

            else:
                messages.warning(request, 'Worng username or password')


    context = {
        "form" : form
    }
    return render(request, 'user/login.html', context)




def logout_user(request):
    logout(request)
    return redirect('login')




@not_logged_in_required
def signup(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            messages.success(request, "Registration sucessful")
            login(request, user)
            return redirect('home')
        

    context = {
        "form": form
    }

    return render(request, 'user/signup.html', context)








def profile(request):
    account = get_object_or_404(User, pk=request.user.pk)


    queryset = request.user.user_blogs.all()
    page = request.GET.get('page', 1)
    # enter how many post you want to see on single page
    paginator = Paginator(queryset, 6)

    delete = request.GET.get('delete', None)

    if delete:
        blog = get_object_or_404(Blog, pk = delete)
        if request.user.pk != blog.user.pk:
            return redirect('home')
        blog.delete()
        messages.success(request, 'Your blog han been delete')
        return redirect('profile')


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
        "account": account,
    }
    return render(request, 'user/profile.html', context)





@login_required(login_url='login')
def edit_profile(request):
    account = get_object_or_404(User, pk=request.user.pk)
    form = UserProfileUpdateForm(instance=account)
    
    if request.method == "POST":
        if request.user.pk != account.pk:
            return redirect('home')
        
        form = UserProfileUpdateForm(request.POST, instance = account)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile has been updated sucessfully")
            return redirect('profile')
        else:
            print(form.errors)

    context = {
        "account": account,
        "form": form
    }
    return render(request, 'user/editProfile.html', context)



@login_required(login_url='login')
def change_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['profile_image']
            user = get_object_or_404(User, pk = request.user.pk)

            if request.user.pk != user.pk:
                return redirect('home')
            

            user.profile_image = image
            user.save()
            messages.success(request, 'Profile picture updated Successfully')
            return redirect('profile')
        
        
        
    return redirect('edit_profile')






@login_required(login_url='login')
def add_blog(request):
    form = AddBlogForm()

    if request.method == 'POST':
        form = AddBlogForm(request.POST, request.FILES)
        if form.is_valid():
            tags = request.POST['tags'].split(',')
            user = get_object_or_404(User, pk = request.user.pk)
            category = get_object_or_404(Category, pk = request.POST['category'])
            blog = form.save(commit= False)
            blog.user = user
            blog.category = category
            blog.save()

            for tag in tags:
                tag_input = Tag.objects.filter(
                    title__iexact = tag.strip(),
                    slug = slugify(tag.strip())
                    )
                
                if tag_input.exists():
                    t = tag_input.first()
                    blog.tags.add(t)

                else:
                    new_tag = Tag.objects.create(
                        title = tag.strip(),
                        slug = slugify(tag.strip())
                    )
                    blog.tags.add(new_tag)


            messages.success(request, 'Blog Added Successfully')
            return redirect('blog_details', slug = blog.slug)
        
        else:
            print('-----------------------', form.errors,'-------------------')



    ontext = {
        "form": form
    }
    return render(request, 'blogs/add_post.html', ontext)










@login_required(login_url='login')
def update_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    form = AddBlogForm(instance=blog)

    if request.method == "POST":
        form = AddBlogForm(request.POST, request.FILES, instance=blog)
        
        if form.is_valid():
            
            if request.user.pk != blog.user.pk:
                return redirect('home')

            tags = request.POST['tags'].split(',')
            user = get_object_or_404(User, pk=request.user.pk)
            category = get_object_or_404(Category, pk=request.POST['category'])
            blog = form.save(commit=False)
            blog.user = user
            blog.category = category
            blog.save()

            for tag in tags:
                tag_input = Tag.objects.filter(
                    title__iexact=tag.strip(),
                    slug=slugify(tag.strip())
                )
                if tag_input.exists():
                    t = tag_input.first()
                    blog.tags.add(t)

                else:
                    if tag != '':
                        new_tag = Tag.objects.create(
                            title=tag.strip(),
                            slug=slugify(tag.strip())
                        )
                        blog.tags.add(new_tag)

            messages.success(request, "Blog updated successfully")
            return redirect('blog_details', slug=blog.slug)
        else:
            print(form.errors)


    context = {
        "form": form,
        "blog": blog
    }
    return render(request, 'blogs/update_blog.html', context)












def view_user_information(request, username):
    account = get_object_or_404(User, username = username)
    blogs = account.user_blogs.all()


    queryset = Blog.objects.order_by('-created_date')
    page = request.GET.get('page', 1)
    # enter how many post you want to see on single page
    paginator = Paginator(queryset, 3)



    delete = request.GET.get('delete', None)
    if delete:
        blog = get_object_or_404(Blog, pk = delete)
        if request.user.pk != blog.user.pk:
            return redirect('home')
        blog.delete()
        messages.success(request, 'Your blog han been delete')
        return redirect('profile')
    
    

    try:
        blogs = paginator.page(page)

    except EmptyPage:
        blogs = paginator.page(1)

    except PageNotAnInteger:
            blogs = paginator.page(1)
            return redirect('blogs')


    

    following = False
    if request.user.is_authenticated:
        if request.user.id == account.id:
            return redirect('profile')
        followers = account.followers.filter(followed_by__id = request.user.id)
        if followers.exists():
            following = True



    context = {
        'blogs': blogs,
        'paginator': paginator,
        'account' : account,
        'following' : following,
        
    }

    return render(request, 'user/profile.html', context)






@login_required(login_url='login')
def follow_or_unfollow_user(request, user_id):
    followed = get_object_or_404(User, id = user_id)
    followed_by = get_object_or_404(User, id = request.user.id)
    follow, created = Follow.objects.get_or_create(
        followed = followed, 
        followed_by = followed_by
    )

    if created:
        followed.followers.add(follow)

    else:
        followed.followers.remove(follow)
        follow.delete()

    return redirect('view_user_information', username = followed.username)
