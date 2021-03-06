# get_object_or_404 this function will try to get an object, and it doest throws a 404 error
from django.shortcuts import render,get_object_or_404
from .models import Post 

# # Create your views here.
def all_blogs (request):
    #posts = Post.objects.all()
    posts = Post.objects.order_by('-date') #orders the 5 most recent postings
    return render(request, 'blog/all_blogs.html', {'posts':posts})
#the id that is being passed is the nth blog number
#the number will be passed to the html and then be displayed
def detail (request,blog_id):
    #pass in name of the class: Blog, and the primary key
    post = get_object_or_404(Post,pk=blog_id)
    return render(request, 'blog/detail.html', {'post':post})


# <!-- <a href="{% url 'detail'%}"></a> -->