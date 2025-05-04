from django.db import models

class Material(models.Model):
    TYPE_CHOICES = [
        ('file', 'Файл'),
        ('image', 'Зображення'),
        ('youtube', 'YouTube'),
        ('link', 'Посилання'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    material_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    file = models.FileField(upload_to='materials/files/', blank=True, null=True)
    image = models.ImageField(upload_to='materials/images/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
