from django import forms
from django.core.exceptions import ValidationError

from .models import Post

class PostForm(forms.ModelForm):
    text_author = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = ['author', 'category', 'title', 'text_author']