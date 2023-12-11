from django.contrib import admin

# Register your models here.

from .models import BlogModel,profile

admin.site.register(BlogModel)
admin.site.register(profile)
