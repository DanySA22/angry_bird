from django.db import models

# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=255)
    score = models.IntegerField()
    email = models.EmailField(max_length=300, default='testing@angrybird.com')
    # profile_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    rating = models.IntegerField()
    # full_name = ['first_name' + ' ' + 'last_name']
   
    
    def __str__(self) -> str:
        return self.username
    
    
#class Dificulty(models.Model):
     #level = models.CharField(max_length=255)
  #  customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=2)
 #this hold the level dificulty by user. I want set that
 #when user click on the level this POST on this table the level and then 
 #when user sign in or auth will conect the user ino with the level.
    
     #def __str__(self) -> str:
       # return self.level