from django.db import models

# represent the portfolio projects
#adding this to our data base
class Project(models.Model):
    #max_length - the title of projects can never have a charater length more than a 100
    title = models.CharField(max_length=100)
    #description of each project has a max of 250 chars
    description = models.CharField(max_length=250)
    #allows us to upload images, to specified folder
    #in this case it goes to portfolio/images/
    image = models.ImageField(upload_to='portfolio/images/')
    #clickable on the portfolio
    url = models.URLField(blank=True) #blank in this case means its
    #not necssary to add an image with characters

    #function to show the names of each blog that created for the admin
    #returns the default name of the object created in admin when looking at a object
    def __str__(self):
        return self.title