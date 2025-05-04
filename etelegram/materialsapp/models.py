import os
from django.db import models
from django.core.exceptions import ValidationError





class Material(models.Model):
    TYPE_CHOICES = [
        ('file', 'Файл'),
        ('image', 'Зображення'),
        ('youtube', 'YouTube'),
        ('link', 'Посилання'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    media = models.FileField(upload_to='galery/')
    url = models.URLField(blank=True, null=True)
    material_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='file')  # Add this line
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    @property
    def is_image(self):
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        ext = os.path.splitext(self.media.name)[1].lower()
        return ext in image_extensions

    @property
    def is_video(self):
        video_extensions = ['.mp4', '.avi', '.mov']
        ext = os.path.splitext(self.media.name)[1].lower()
        return ext in video_extensions
    
