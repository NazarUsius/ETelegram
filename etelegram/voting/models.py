from django.db import models
from django.conf import settings


class Voting(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=70, blank = True, null = True)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"Voting: {self.title}"

class Answer(models.Model):
    title = models.CharField(max_length=30)

class UserAnswer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

class Session(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='voting_sessions')
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE)


