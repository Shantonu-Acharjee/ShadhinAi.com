from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .decorators import not_logged_in_required
from post.models import Blog
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator


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
    return render(request, 'user/profile.html', context)


def edit_profile(request):
    return render(request, 'user/editProfile.html')
