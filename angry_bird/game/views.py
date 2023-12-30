from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.utils import timezone
from .models import Customer
from .serializer import CustomerEmailSerializer, CustomerFirstnameSerializer, CustomerImageSerializer, CustomerLastnameSerializer, CustomerPasswordSerializer, CustomerRatingSerializer, CustomerScoreSerializer, CustomerUsernameSerializer, CustomerFormSerializer, CustomerAuthenticationSerializer, UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
 
# Create your views here. 

#RELATED TO GAMEPAGE

class ScoreSave(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def put(self, request):
        user_profile = Customer.objects.get(user=request.user)
        serializer = CustomerScoreSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
         
 
     
        
'''A View that GET user profile images if user isAuthenticated && uploaded a photo already otherwise 
just render the generic empty image. I should set on th model image field 
this empty profile image as default. Here you just need to add the image field data for that user
on JS we set the particular element to change the img source for what is retrieve from backend
through axios. 
FOR NOW will be only on empty profile, I will not set up this view or the related frontend
''' 
    

#RELATED TO PROFILE PAGE (USER CAN ONLY ACCESS THIS PAGE IF IT IS AUTHENTICATED)

class FormProfile(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user_profile = request.user
        serializer = CustomerFormSerializer(user_profile) 
        return Response(serializer.data)
    
    def put(self, request):
        user_profile = request.user
        serializer = CustomerFormSerializer(user_profile, data=request.data) 
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        
        
class UserScore(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        persona = Customer.objects.get(user=request.user)
        serializer = CustomerScoreSerializer(persona) 
        return Response(serializer.data) 

class UserRating(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request):
        persona = Customer.objects.get(user=request.user)
        serializer = CustomerRatingSerializer(persona, data=request.data) 
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
 


 #RELATED TO SIGN UP PAGE        

class UserSignin(APIView): 
    def post(self, request, format=None): 
        serializer = UserSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

#RELATED TO AUTHENTICATION PAGE

class UserAuthentication(APIView):
    def post(self, request):
        username = request.data.get("username") # It's used to retrieve the value associated with the specified key, in this case, "username".
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            user.last_login = timezone.now()
            user.save(update_fields=['last_login'])
            # Delete existing token if it exists
            Token.objects.filter(user=user).delete()

            # Create a new token
            token = Token.objects.create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

'''Django's authenticate function, which checks if the username and password are valid. 
If the credentials are valid, it returns a User object; otherwise, it returns None.
If user is not None (meaning authentication is successful), a token is either retrieved or 
created for the user. This is typically used for token-based authentication in APIs.
Token.objects.get_or_create(user=user) either gets an existing token for the user or 
creates a new one.

The HTML form should submit to the endpoint of the corresponding view.
Make sure that the 'name' on the form field match with the name of your serializer fields
'''

#LOG OUT

class UserLogout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # This will only be executed if the user is authenticated
        try:
            request.user.auth_token.delete()
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except (AttributeError, Token.DoesNotExist):
            return Response({"error": "Invalid token / already logged out"}, status=status.HTTP_400_BAD_REQUEST)