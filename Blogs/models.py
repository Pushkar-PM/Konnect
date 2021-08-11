from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.conf import settings


class Blogs(models.Model):
    title=models.CharField(max_length=50)
    blogs=RichTextField(blank=True,null=True,verbose_name='')
    # blogs=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    upvotes=models.ManyToManyField(User,related_name="upv")
    # upvotes=models.ForeignKey(User, verbose_name='', on_delete=models.CASCADE,related_name='upv')

    def get_absolute_url(self):
        return reverse('blogs')

class Comments(models.Model):
    author=models.ForeignKey(User, verbose_name='', on_delete=models.CASCADE,related_name='writer')
    post=models.ForeignKey(Blogs, verbose_name='', on_delete=models.CASCADE,related_name='comment')
    comment=models.TextField()

    # def get_absolute_url(self):
    #     return reverse('comments',kwargs={'pk':post})
    

