from django.db import models

# Create your models here.
class Gallery(models.Model):
    name = models.CharField()
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
