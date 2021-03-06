"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#adding a path so that we can access blog files
from django.urls import include

#add functionality from the django project
from django.conf.urls.static import static

#import the settings file here
from django.conf import settings

#import portfolio views
from portfolio import views


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.home, name = 'home'),
    path('blog/', include('blog.urls')),
]
#can look up django media images, takes the url where the admin would add images
#goes into the media root directory where the image is currently stored
urlpatterns+= static(settings.MEDIA_URL, document_root =  settings.MEDIA_ROOT)


