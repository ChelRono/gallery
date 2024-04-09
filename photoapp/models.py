from django.db import models

IMG_CHOICES = (
    ('JPG','jpg'),
    ('PNG','png'),
    ('JPEG','jpeg'),
    
)

# Create your models here.
class Gallery(models.Model):
    name = models.CharField()
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    option = models.CharField(max_length=6, choices=IMG_CHOICES, default='JPG')
