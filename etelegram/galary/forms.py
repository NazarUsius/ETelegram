from django import forms

from .models import Media

class MediaForm(forms.ModelForm):
    media = forms.FileField()

    class Meta:
        model = Media
        fields = ["media"]