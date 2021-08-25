from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Register

class UserRegisterForm(UserCreationForm):
   email=forms.EmailField()
   
   class Meta:
       model=User
       fields=['username','email','password1','password2']
    
class Register(forms.ModelForm):
        
        class Meta:
            model = Register
            fields = ('department','year_of_study')
    


    