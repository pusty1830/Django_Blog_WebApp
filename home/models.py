from django.db import models

from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .healpers import *

class profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_varified=models.BooleanField(default=False)
    token=models.CharField(max_length=100)



class BlogModel(models.Model):
    title=models.CharField(max_length=1000)
    content=FroalaField()
    slug=models.SlugField(max_length=1000,null=True,blank=True)
    image=models.ImageField(upload_to='blog')
    user=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
  
    def __str__(self) :
        return self.title
    def save(self,*args,**kwargs):
        self.slug=generateslug(self.title)
        super(BlogModel,self).save(*args,**kwargs)
