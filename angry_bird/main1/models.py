from django.db import models

# Create your models here.

class Dificulty(models.Model):
    level = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.level