from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Slider
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    # load all the slider from db
    sliders = Slider.objects.all()

    data = {
        'sliders' : sliders,
    }
    return render(request, 'home.html', data)



def projects(request):
    return render(request, 'projects.html')



def blogs(request):
    return render(request, 'blogs.html')



def sitemap(request):
    return render(request, 'sitemap.html')



def login(request):
    return render(request, 'login.html')


def signup(request):

    if request.method == 'POST':

        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_password1 = request.POST.get("user_password1")
        user_password2 = request.POST.get("user_password2")


        #my_user = User.objects.create_user(user_name, user_email, user_password1)
        #my_user.save()

        print(user_name, user_email, user_password1, user_password2)

    return render(request, 'signup.html')


def userProfile(request):
    return render(request, 'userProfile.html')