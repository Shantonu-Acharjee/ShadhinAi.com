from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages

def login(request):
    return render(request, 'user/login.html')


def signup(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            messages.success(request, "Registration sucessful")
            return redirect('login')
        

    context = {
        "form": form
    }

    return render(request, 'user/signup.html', context)