from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
from Users.models import Register
from django.urls import reverse
from PIL import Image
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey 


class Blogs(models.Model):
    title=models.CharField(max_length=50)
    blogs=RichTextField(blank=True,null=True,verbose_name='')
    # blogs=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    upvotes=models.ManyToManyField(User,related_name="upv")
    globalblog=models.BooleanField(default=False)
    # upvotes=models.ForeignKey(User, verbose_name='', on_delete=models.CASCADE,related_name='upv')

    def get_absolute_url(self):
        return reverse('blogs')


class Comment(MPTTModel):
    author = models.ForeignKey(User, related_name='author',
                               on_delete=models.CASCADE, default=None, blank=True)
    post = models.ForeignKey(Blogs,
                             on_delete=models.CASCADE,
                             related_name='comments')
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['publish']




