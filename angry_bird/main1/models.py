from django.db import models
from game.models import Customer
# Create your models here.

class Dificulty(models.Model):
     level = models.CharField(max_length=255)
  #  customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=2)
    
     def __str__(self) -> str:
        return self.level
