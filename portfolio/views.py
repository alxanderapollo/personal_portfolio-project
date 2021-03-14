from django.shortcuts import render
from .models import Project #want to display all the content stored in the DATABASE  

# Create your views here.
def home(request):
    #get alls the projects from the database
    #we then pass it as a param to display on the home page
    projects = Project.objects.all() 
    return render(request, 'portfolio/home.html', {'projects':projects})

# def blog (request):
#     return render(request, '/blog/views.py')