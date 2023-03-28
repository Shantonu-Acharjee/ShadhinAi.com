from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.


def login(request):
    return render(request, 'login.html')


def signup(request):

    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user_obj = User.objects.filter(username = email)


        if user_obj.exists():
            messages.warning(request, 'Email alrady taken.')


        elif password1 != password2:
            messages.warning(request, 'Password Not mach')


        else:
            user_obj = User.objects.create(first_name = first_name, last_name = last_name, email = email, username = email)
            user_obj.set_password(password1)
            user_obj.save()
            messages.success(request, 'Your Account Created')
        
            return redirect('login')
        

    return render(request, 'signup.html')
