from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    dicription = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    