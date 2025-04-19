from django import forms
from .models import *

class QuizForm(forms.ModelForm):
    title = forms.CharField(max_length=15)
    description = forms.CharField(max_length=25, required=False)
    rating = forms.IntegerField(required=False)

    class Meta:
        model = Quiz
        fields = ["title", "description", "rating"]

class SectionForm(forms.ModelForm):
    title = forms.CharField(max_length=15)
    description = forms.CharField(max_length=25, required=False)

    class Meta:
        model = Section
        fields = ["title", "description"]

class QuestionForm(forms.ModelForm):
    KINDS_OF_QUESTION = [("tf", "Text fill"), ("c", "Choice")]

    title = forms.CharField(max_length=25)
    kind = forms.ChoiceField(choices=KINDS_OF_QUESTION)
    class Meta:
        model = Question
        fields = ["title", "kind"]

class AnswerForm(forms.ModelForm):
    KINDS_OF_ANSWER = [("c", "Correct"), ("i", "Incorrect")]

    title = forms.CharField(max_length=25)
    correctness = forms.ChoiceField(choices=KINDS_OF_ANSWER)
    class Meta:
        model = Answer
        fields = ["title", "correctness"]