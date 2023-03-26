from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')



def projects(request):
    return render(request, 'projects.html')



def blogs(request):
    return render(request, 'blogs.html')