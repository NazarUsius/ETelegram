from django import forms
from django.core.exceptions import ValidationError

from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=20)
    description = forms.CharField(max_length=300)
    media = forms.ImageField()


    class Meta:
        model = Post
        fields = ["title", "description", "media"]