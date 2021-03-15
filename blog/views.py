from django.shortcuts import render
from .models import Post 

# # Create your views here.
def all_blogs (request):
    post = Post.objects.order_by('-date')[:5] #orders the 5 most recent postings
    return render(request, 'blog/all_blogs.html', {'post':post})