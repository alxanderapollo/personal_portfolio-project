from django.db import models

# Create your models here.
class Post(models.Model):
    #max_length - the title of projects can never have a charater length more than a 100
    title = models.CharField(max_length=200)
    #description of each project has a max of 250 chars
    date = models.DateField()
    #clickable on the portfolio
    
    description = models.TextField()
    
    url = models.URLField(blank=True) #blank in this case means its
    #not necssary to add an image with characters
    
    #function to show the names of each blog that created for the admin
    #returns the default name of the object created in admin when looking at a object
    def __str__(self):
        return self.title

    