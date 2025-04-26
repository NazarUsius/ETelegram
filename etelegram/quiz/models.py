from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# for creating a quiz:
class Quiz(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField(max_length=25, null=True, blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Quiz {self.title}"

class Section(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField(max_length=25, null=True, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return f"Section {self.title} requires to {self.quiz}"

class Question(models.Model):
    KINDS_OF_QUESTION = {"tf":"Text fill",
                         "c":"Choice"}

    title = models.CharField(max_length=25)
    kind = models.CharField(max_length=25, choices=KINDS_OF_QUESTION)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Question {self.title}"

class Answer(models.Model):
    KINDS_OF_ANSWER = {"c":"Correct",
                       "i":"Incorrect"}
    title = models.CharField(max_length=25)
    correctness = models.CharField(max_length=25, choices=KINDS_OF_ANSWER, default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"Answer {self.title} is {self.correctness}"

#for answering

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user}---{self.quiz}"
class UserAnswer(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_response = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.session.user} --- {self.question} ---- {self.selected_answer}"

