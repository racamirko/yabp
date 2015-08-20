from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Story(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    date = models.TimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

