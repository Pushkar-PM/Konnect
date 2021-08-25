from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegisterForm,Register
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls  import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
posts=[
    {
        'author':'Pushakr',
        'msg':'Hello'
    }
]

def register(request):
    context={
        'user':UserRegisterForm,
        'register':Register,
        # 'extra':ExtraReg
    }
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        rform=Register(request.POST)
        if form.is_valid() and rform.is_valid():
            user=form.save()
            e=rform.save(commit=False)
            e.user=user
            e.save()
            messages.success(request,f'Login now')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'Users/user.html',context)
