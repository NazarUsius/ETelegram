from django.db import models
from django.contrib.auth.models import User, Group

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Чоловік'),
        ('female', 'Жінка'),
        ('other', 'Інше'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"Профіль: {self.user.username}"
