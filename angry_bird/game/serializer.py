from rest_framework import serializers
from game.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username', 'score', 'rating', 'email', 'first_name', 'last_name', 'profile_image', 'password']
                  
class CustomerUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username']

class CustomerScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['score']
        
class CustomerRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['rating']
        
class CustomerEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['email']
        
class CustomerFirstnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name']
        
class CustomerLastnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['last_name']
        
class CustomerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['profile_image']
        
class CustomerPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['password']        

class CustomerFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        
class CustomerAuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username', 'password']