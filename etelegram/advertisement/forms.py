from django import forms
from .models import Advertisement

class AddCreate(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'media', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'media': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ApproveAddCreate(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'media', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'media': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
