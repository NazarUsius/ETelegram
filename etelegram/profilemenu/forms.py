from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'gender', 'birth_date', 'email']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
