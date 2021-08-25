from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Blogs,Comment
from django.views import View
from .forms import CreateBlogs,NewCommentForm
from django.core.paginator import Paginator

# Create your views here.

class PostCreate(LoginRequiredMixin,CreateView):
    model=Blogs
    form_class=CreateBlogs

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)       

class BlogsView(LoginRequiredMixin,ListView):
    # context_object_name='blogs-comment'
    paginate_by=1

    def get_queryset(self):
        return Blogs.objects.all()


    def get_context_data(self, **kwargs):
        context = super(BlogsView, self).get_context_data(**kwargs)
        context['blogs'] = Blogs.objects.all()
        context['comment_form']=NewCommentForm()
        # print(Blogs.pk)
        return context

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
            

def addcomment(request):

    if request.method == 'POST':
            comment_form = NewCommentForm(request.POST)
            print(comment_form)
            if comment_form.is_valid():
                user_comment = comment_form.save(commit=False)
                result = comment_form.cleaned_data.get('content')
                user = request.user.username
                user_comment.author = request.user
                user_comment.save()
                return JsonResponse({'result': result, 'user': user})
            else:
                print(comment_form.errors)



# def displaymore(request):

#     postid=0
#     template_name='Blogs/comment.html'
#     allcomments=''

#     if request.method=='POST':
#         postid=request.POST['postid']
#         post=get_object_or_404(Blogs,id=postid)
#         allcomments=post.comments.filter(status=True)
    
#     return render(request,'Blogs/comment.html',{'allcomments':allcomments})
        

#     def get_context_data(self, **kwargs):
#         context = super(displaymore, self).get_context_data(**kwargs)
#         context['allcomments']=allcomments
#         # print(Blogs.pk)
#         return context







