from django import forms
from datetime import datetime

class EventForm(forms.Form):
    summary = forms.CharField(label="Назва події", max_length=255)
    description = forms.CharField(widget=forms.Textarea, label="Опис", required=False)
    start = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), label="Початок")
    end = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), label="Кінець")

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start")
        end = cleaned_data.get("end")
        if start and end and start >= end:
            raise forms.ValidationError("Кінець події повинен бути пізніше початку.")
        return cleaned_data