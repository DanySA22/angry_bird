from django.db import models

# Create your models here.



class Customer(models.Model):
    first_name = models.CharField(max_length=255, default= 'Pedro')
    last_name = models.CharField(max_length=255, default= 'Ramirez')
    username = models.CharField(max_length=255)
    score = models.IntegerField()
    email = models.EmailField(max_length=300, default='testing@angrybird.com')
    profile_image = models.ImageField(height_field=None, 
    width_field=None, max_length=300, blank=True)
    rating = models.IntegerField()
    password =models.CharField(max_length=30, default= 'AngryBird24$')
#    add a password field
    
    def __str__(self) -> str:
        return self.username
    
    
