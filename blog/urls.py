from django.urls import path

#adding a path so that we can access blog files
from django.urls import include

#dont need views because we are in the same folder can use only just . and itll be fine
from . import views


urlpatterns = [ 
    path('', views.all_blogs, name = 'all_blogs'),
    path('<int:blog_id>/', views.detail, name = 'detail'),
]