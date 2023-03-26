from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Slider

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
    return render(request, 'signup.html')


def userProfile(request):
    return render(request, 'userProfile.html')