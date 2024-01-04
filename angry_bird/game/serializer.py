from rest_framework import serializers
from game.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  
    # Write only to ensure password its not included in te serializer output

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
# This create method is called when you save a serializer instance using .save() 
# if creating a new instance (as opposed to updating an existing instance). 
# User.objects.create_user() is a helper method provided by Django's
# User model that creates a new user instance. The method also handles important aspects 
# like hashing the password. **validated_data unpacks the validated data into the function 
# call as arguments.  return user: Finally, the newly created user object is returned.

class CustomerFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def update(self, instance, validated_data):
        # Check if 'password' is in validated_data and hash it if present
        if 'password' in validated_data:
            raw_password = validated_data.pop('password')
            hashed_password = make_password(raw_password)
            instance.password = hashed_password

        # Update other fields normally
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
             
class CustomerUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
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
        model = User
        fields = ['email']
        
class CustomerFirstnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name']
        
class CustomerLastnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['last_name']
        
class CustomerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['profile_image']
        
class CustomerPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password']        


        
class CustomerAuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']