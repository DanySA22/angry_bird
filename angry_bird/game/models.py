from django.db import models
from main1.models import Dificulty
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    score = models.IntegerField()
    # profile_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    rating = models.IntegerField()
    # full_name = ['first_name' + ' ' + 'last_name']
    dificulty = models.ManyToManyField(Dificulty)
    
    def __str__(self) -> str:
        return self.first_name