from django.contrib import admin
from .models import UserProfile, BlogPost

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(BlogPost)
