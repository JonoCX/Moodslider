from django.db import models

# Create your models here.

class Programme(models.Model):
    programme_id = models.IntegerField()
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    mood = models.CharField(max_length=50)
