from django.db import models
from django.utils import timezone

class Announcement(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата створення')

    def __str__(self):
        return self.title
    


