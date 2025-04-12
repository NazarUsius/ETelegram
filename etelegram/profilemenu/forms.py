from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # Указание модели
        fields = ['avatar', 'birth_date', 'email', 'gender']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
