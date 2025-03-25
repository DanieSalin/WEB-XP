from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    producer = models.CharField(max_length=200)
    duration = models.IntegerField()
    director = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='movies/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
