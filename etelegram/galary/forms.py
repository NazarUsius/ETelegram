from django import forms

from .models import Media

class MediaForm(forms.ModelForm):
    media = forms.FileField()
    title = forms.CharField(max_length=255, required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)


    class Meta:
        model = Media
        fields = ["media", "title", "description"]