from django import forms
from .models import *

class VotingForm(forms.ModelForm):
    title = forms.CharField(max_length=15)
    description = forms.CharField(max_length=25, required=False)
    rating = forms.IntegerField(required=False)

    class Meta:
        model = Voting
        fields = ["title", "description", "rating"]

class AnswerForm(forms.ModelForm):
    title = forms.CharField(max_length=15)

    class Meta:
        model = Answer
        fields = ["title"]