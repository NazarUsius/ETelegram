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



class Portfolio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    media = models.FileField(upload_to='portfolio/', validators=[validate_file_extension])
    hided = models.BooleanField(default=False)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    

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

