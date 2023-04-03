from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .decorators import not_logged_in_required



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