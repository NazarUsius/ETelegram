from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

from .models import Grade, Subject, EvaluationType


class GradeForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select()
    )
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.Select()
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    evaluation_type = forms.ChoiceField(
        choices=EvaluationType.choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    grade = forms.IntegerField(
        min_value=1,
        max_value=12,
        widget=forms.NumberInput()
    )

    class Meta:
        model = Grade
        fields = ['user', 'subject', 'date', 'evaluation_type', 'grade']

    def clean_grade(self):
        grade = self.cleaned_data.get('grade')
        if not 1 <= grade <= 12:
            raise ValidationError("Оценка должна быть от 1 до 12.")
        return grade

