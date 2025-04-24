from django.db import models
from django.conf import settings

class Media(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    media = models.FileField(upload_to='galary/')