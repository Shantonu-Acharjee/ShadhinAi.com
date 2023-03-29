from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Slider, Post
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    # load all the slider from db
    sliders = Slider.objects.all()
    posts = Post.objects.all()

    data = {
        'sliders' : sliders,
        'posts' : posts,
    }


    return render(request, 'home.html', data)



def projects(request):
    return render(request, 'projects.html')



def blogs(request):
    return render(request, 'blogs.html')



def sitemap(request):
    return render(request, 'sitemap.html')






def userProfile(request):
    return render(request, 'userProfile.html')



def photoGallery(request):
    return render(request, 'photoGallery.html')




def post(request):
    return render(request, 'post.html')









