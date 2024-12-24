from django.db import models

# Create your models here.
class Destination(models.Model):  # Use PascalCase for model names
    name = models.CharField(max_length=100)
    country = models.TextField()
    review = models.IntegerField(default=0)
    days = models.IntegerField(default=0)
    stars = models.IntegerField(default=0)
    image_name = models.ImageField(upload_to='images/')
    offer = models.BooleanField(default=False)
