from django.contrib import admin
#import our models in here
from .models import Project
# here we show what models show up inside of the admin
admin.site.register(Project)
#save and this will now show up on admin pages