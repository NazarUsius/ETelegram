from django.db import models

from django.db import models
from django.contrib.auth.models import User



class GoogleCredentials(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='google_credentials')
    token_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Google Credentials for {self.user.username}"
