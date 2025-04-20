from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class EvaluationType(models.TextChoices):
    TEST = 'Контрольна'
    QUIZ = 'Самостійна'
    HOMEWORK = 'Домашнє завдання'
    OTHER = 'Інше'

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    evaluation_type = models.CharField(max_length=50, choices=EvaluationType.choices)
    grade = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.grade}"