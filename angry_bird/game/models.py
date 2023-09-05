from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    score = models.IntegerField()
    profile_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    rating = models.IntegerField()