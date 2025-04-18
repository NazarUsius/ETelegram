from django import forms
from .models import *

class QuizForm(forms.Form):
    title = forms.CharField(max_length=15)
    description = forms.CharField(max_length=25, null=True, blank=True)
    rating = forms.IntegerField(null=True, blank=True)

    class Meta:
        model = Quiz
        fields = ["title", "description", "rating"]

class SectionForm(forms.Form):
    title = forms.CharField(max_length=15)
    description = forms.CharField(max_length=25, null=True, blank=True)

    class Meta:
        model = Section
        fields = ["title", "description"]

class QuestionForm(forms.Form):
    KINDS_OF_QUESTION = {"tf": "Text fill",
                         "c": "Choice"}

    title = forms.CharField(max_length=25)
    kind = forms.CharField(max_length=25, choices=KINDS_OF_QUESTION)
    class Meta:
        model = Question
        fields = ["title", "kind"]

class AnswerForm(forms.Form):
    KINDS_OF_ANSWER = {"c": "Correct",
                      "i": "Incorrect"}
    title = forms.CharField(max_length=25)
    correctness = forms.CharField(max_length=25, choices=KINDS_OF_ANSWER)
    class Meta:
        model = Answer
        fields = ["title", "correctness"]