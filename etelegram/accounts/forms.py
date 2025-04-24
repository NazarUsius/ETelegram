from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "avatar", "gender", "birth_date")
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }


