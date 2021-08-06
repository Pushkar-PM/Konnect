from django.shortcuts import render
from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Blogs
# Create your views here.

class PostCreate(LoginRequiredMixin,CreateView):
    model=Blogs
    fields=['blogs']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)       

class BlogsView(LoginRequiredMixin,ListView):
    model=Blogs

def upvote(request):
    if request.method=='POST':
        r=request.POST['blog']
        if(Blogs.objects.get(pk=r).upvotes.filter(username=request.user).count()==0):
            b1=Blogs.objects.get(pk=r)
            b1.upvotes.add(request.user)
            print(request.user.username)
            print("jkdhw")
            b1.save()
            return JsonResponse({'bool':True})
        else:
            Blogs.objects.get(pk=r).upvotes.remove(request.user)
            return JsonResponse({'bool':False})
    return JsonResponse({'bool':False})