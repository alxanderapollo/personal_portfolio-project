from django.db import models

# Create your models here.
class Post(models.Model):
    #max_length - the title of projects can never have a charater length more than a 100
    title = models.CharField(max_length=100)
    #description of each project has a max of 250 chars
    date = models.CharField(max_length=250)
    
    #clickable on the portfolio
    url = models.URLField(blank=True) #blank in this case means its
    #not necssary to add an image with characters

    