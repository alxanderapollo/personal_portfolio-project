from django.contrib import admin

# Register your models here.
from django.contrib import admin
#import our models in here
from .models import Post
# here we show what models show up inside of the admin
admin.site.register(Post)
#save and this will now show up on admin pages