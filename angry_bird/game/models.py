from django.db import models

# Create your models here.

class Dificulty(models.Model):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'

    LEVEL_CHOICES = [
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    ]
    
    level = models.CharField(
        max_length=255, choices=LEVEL_CHOICES, default=EASY)
 
 
  #  customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=2)
 #this hold the level dificulty by user. I want set that
 #when user click on the level this POST on this table the level and then 
 #when user sign in or auth will conect the user ino with the level.
    
    def __str__(self) -> str:
       return self.level

class Customer(models.Model):
    first_name = models.CharField(max_length=255, default= 'Pedro')
    last_name = models.CharField(max_length=255, default= 'Ramirez')
    username = models.CharField(max_length=255)
    score = models.IntegerField()
    email = models.EmailField(max_length=300, default='testing@angrybird.com')
    profile_image = models.ImageField(height_field=None, 
    width_field=None, max_length=300, blank=True)
    rating = models.IntegerField()
    dificulty = models.ForeignKey(Dificulty, on_delete=models.CASCADE, null=True)
   
    
    def __str__(self) -> str:
        return self.username
    
    
