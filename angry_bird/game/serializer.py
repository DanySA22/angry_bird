from rest_framework import serializers
from game.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username', 'score', 'rating', 'email', 'first_name', 'last_name', 'profile_image', 'dificulty']
                  
                 