import os
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    """Validates that the uploaded file has an allowed extension."""
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.mp4', '.avi', '.mov']
    if ext not in valid_extensions:
        raise ValidationError(f"Unsupported file extension: {ext}. Allowed extensions are: {', '.join(valid_extensions)}")

class Media(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    media = models.FileField(upload_to='galery/', validators=[validate_file_extension])
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Media: {self.title or self.media.name} by {self.author.username}"

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
