from django.shortcuts import render
from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Blogs,Comments
from django.views import View
from .forms import CreateBlogs
# Create your views here.

class PostCreate(LoginRequiredMixin,CreateView):
    model=Blogs
    form_class=CreateBlogs

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)       

class BlogsView(LoginRequiredMixin,ListView):
    context_object_name='blogs-comment'

    def get_queryset(self):
        return Blogs.objects.all()


    def get_context_data(self, **kwargs):
        context = super(BlogsView, self).get_context_data(**kwargs)
        context['blogs'] = Blogs.objects.all()
        print(Blogs.pk)
        return context

# def upvote(request):
#     if request.method=='POST':
#         r=request.POST['blog']
#         if(Blogs.objects.get(pk=r).upvotes.filter(username=request.user).count()==0):
#             b1=Blogs.objects.get(pk=r)
#             b1.upvotes.add(request.user)
#             print(request.user.username)
#             print("jkdhw")
#             b1.save()
#             return JsonResponse({'bool':True})
#         else:
#             Blogs.objects.get(pk=r).upvotes.remove(request.user)
#             return JsonResponse({'bool':False})
#     return JsonResponse({'bool':False})


class upvote(View):
    def post(self,request):
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

class comment(View):
    def post(self,request):
        r=request.POST['com']
        blog_id=request.POST['blog_id']
        print(r)
        b1=Blogs.objects.get(pk=blog_id)
        c=Comments(author=request.user,post=b1,comment=r)
        c.save()
        print("kkkk")
        return JsonResponse({'bool':True})


