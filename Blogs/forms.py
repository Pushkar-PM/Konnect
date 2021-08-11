from .models import Blogs
from django import forms
    

class CreateBlogs(forms.ModelForm):
    
    class Meta:
        model = Blogs
        fields = ("title","blogs")
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
