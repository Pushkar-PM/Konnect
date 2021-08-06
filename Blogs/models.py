from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Blogs(models.Model):
    blogs=RichTextField(blank=True,null=True)
    # blogs=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    upvotes=models.ManyToManyField(User,related_name="upv")

    def get_absolute_url(self):
        return reverse('blogs')
    

