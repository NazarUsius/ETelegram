from django.db import models

class Advertisement(models.Model):
    STATUS = [
        ("Approved", "Approved"),
        ("In queue", "In queue"),
    ]

    title = models.CharField(max_length=20)
    media = models.ImageField(upload_to='ads/')
    description = models.TextField(max_length=30)
    status = models.CharField(max_length=30, choices=STATUS)

    def __str__(self):
        return f"{self.title} ---> {self.status}"