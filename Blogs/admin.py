from django.contrib import admin
from .models import Blogs,Comment
from mptt.admin import MPTTModelAdmin

# Register your models here.
admin.site.register(Blogs)
admin.site.register(Comment,MPTTModelAdmin)