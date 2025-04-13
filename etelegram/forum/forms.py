from django import forms
from django.core.exceptions import ValidationError

from .models import Branch, LikeBranch, Comment

class BranchForm(forms.ModelForm):
    title = forms.CharField(max_length=20)
    description = forms.CharField(max_length=300)
    media = forms.ImageField()


    class Meta:
        model = Branch
        fields = ["title", "description", "media"]

class LikeBranchForm(forms.ModelForm):
    class Meta:
        model = LikeBranch
        fields = []

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget = forms.Textarea(attrs={'rows': 3, 'placeholder': 'Leave a comment...'})
