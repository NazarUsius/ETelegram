from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    media = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post: {self.title} -> {self.description}"