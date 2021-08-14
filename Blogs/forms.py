from .models import Blogs,Comment
from django import forms
from mptt.forms import TreeNodeChoiceField
    

class CreateBlogs(forms.ModelForm):
    
    class Meta:
        model = Blogs
        fields = ("title","blogs")
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        }


class NewCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update(
            {'class': 'd-none'})

        self.fields['parent'].label = ''
        self.fields['parent'].required = False

    class Meta:
        model = Comment
        fields = ('post', 'parent', 'content')

        widgets = {
            'content': forms.Textarea(attrs={'class': 'ml-3 mb-3 form-control border-0 comment-add rounded-0', 'rows': '1', 'placeholder': 'Add a public comment'}),
        }

    def save(self, *args, **kwargs):
        Comment.objects.rebuild()
        return super(NewCommentForm, self).save(*args, **kwargs)