from django import forms
from django.contrib.auth import get_user_model

from .models import Portfolio, validate_file_extension

User = get_user_model()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'gender', 'birth_date', 'email']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }


class PortfolioCreateForm(forms.ModelForm):
    media = forms.FileField(
        label="Файл",
        help_text="Выберите файл для загрузки (изображение или видео).",
        validators=[validate_file_extension]  # Add the validator here
    )
    title = forms.CharField(
        label="Название",
        max_length=255,
        required=False,
        help_text="Краткое название вашего файла (необязательно)."
    )
    description = forms.CharField(
        label="Описание",
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
        help_text="Добавьте описание к вашему файлу (необязательно)."
    )

    class Meta:
        model = Portfolio
        fields = ['media', 'title', 'description']
