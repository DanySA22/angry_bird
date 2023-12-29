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
 
# Create your views here. The different elements involve in the frontend will use axios and they will interact with the same
# endpoint but doing different methods each case

#RELATED TO GAMEPAGE

''' in this function we should PUT the score that a single user cumulate before he lose.
This means that when user lose not only we will see that pop-up with Game over and the score
but this score will be PUT on user instance DB (it has 1 as score by default). When user check in profile will see
that last PUT of the score. If user is playing without being auth, this info will not be saved.
So this POST/PUT only work if isAuthenticated. 
 So this function should be filter by user playing (id) -OR JUST HAVING THE USER AUTHENTICATED AND WORKING
IN A SESSION - and by the score field.
'''

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
         
'''the post method expects the primary key (pk) of the user 
(this could be passed in the URL), fetches the corresponding user object, 
and then updates it with the provided data. The partial=True argument in the serializer 
allows partial updates, so you don't need to provide all fields of the user.'''   
    
    
    

'''
Just for guidance
@api_view( ['GET', 'POST', 'PUT'])
def game_score(request, pk):
    puntuation = Customer.objects.get(pk=pk)
    serializer = CustomerSerializer(puntuation)
    return Response(serializer.data)  
    elif request.method == 'POST':
        return    
    elif request.method == 'PUT':
        return Response
    else:
        return ('Keep working on it')'''
        
        
'''A View that GET user profile images if user isAuthenticated && uploaded a photo already otherwise 
just render the generic empty image. I should set on th model image field 
this empty profile image as default. Here you just need to add the image field data for that user
on JS we set the particular element to change the img source for what is retrieve from backend
through axios. 
For now will be only on empty profile I will not set up this view or the
related frontend

class UserImage(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        image = Customer.objects.get(user=request.user)
        serializer = CustomerImageSerializer(image) 
#A customed serialized that included only the specific field that I want to return        
        return Response(serializer.data) 

Leter I will need to substitute the the image argument of the serializer for the
request.user (after I set up auth and I add auth and permission class to this view) for
obtaining that particular field data of the auth user''' 
    

#RELATED TO PROFILE PAGE (USER CAN ONLY ACCESS THIS PAGE IF IT IS AUTHENTICATED)

'''I should be able to GET the related user information in the corresponding space 
(when the page load/refresh): 
first name, last name, email, username, password, image.
I should also be able to POST-PUT those informations. I guess I can just 
submit the form as one (only one view) that way the user will see the info; also a
edit botton under each field of the form; but when submit all the form is submitted as one 
(this way I don't need to add more button for submit or change anything on that page 
frontend and diminish the amount of
class views creation and axios creation); and even when get modify complete it will 
only look different on those fields that we changed.

Rating will not have GET only POST-PUT.  
Score only have GET (the last score on the user instance).
'''

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
 

'''
About levels/difficulty:
I don't need to have a model for difficulty or even a field on the same model because:
I am not showcasing the level in the profile page anyway (so for the user the fact 
that I have this information in DB is irrelevant)
Remembering (on DB) difficulty by user then will only important if I want set that every 
time that the user auth, remembers the level and go straight to that but that is not that 
relevant we can set that after auth just go to default easy game page and user can 
change it on profile. I am showcasing already remembering image uploaded which is more 
cool and visible. Besides setting remembering difficulty it is more complicated
I will have to set condition or promises that when this happens render this particular 
endpoint; or if this other choice level happens render this other particular game
endpoint.
In conclusion I will just forget about setting anything in the backend related to 
difficulty and just handle with frontend endpoint redirection. 

Eliminated the level model and relationship; eliminate the class related to level 
handling
    
'''
 
 #RELATED TO SIGN UP PAGE        

'''This will handle POST method of the form. Validation rules could be included (on the back or frontend).
After completion user will be redirected to auth page. Which means that when user
click submit a POST will happend to the backend -if valid the form- and then a redirection will happen to
auth endpoint -this is with a JS async promise (On Axios): after POST then redirect to auth endpoint '''

class UserSignin(APIView): 
    def post(self, request, format=None): 
        serializer = UserSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

#RELATED TO AUTHENTICATION PAGE
'''This will handle POST method of the form and get along with the auth process.
Validation rules could be included (on the back or frontend). When user click submit a 
POST for validation will happen and user will be redirected to the default endpoint of
difficulty level game (easy) -this is with a JS async promise (On Axios): after POST 
then redirect to game(easy) endpoint.
If user want changed the level because is auth, can go from game page to profile
and then if he pick a different level -at the bottom- it will be redirected there.

This way we will have more simplicity: the levels on the mainpage go direct to the game 
even if unauthenticated but if you do it on profile that will redirect as well but auth.

'''

# class UserAuthentication(APIView):
#     def post(self, request, pk):
#         user = get_object_or_404(Customer, pk=pk)
#         serializer = CustomerAuthenticationSerializer(user, data=request.data) 
#         if serializer.is_valid():
#             serializer.save()  
#             return Response(serializer.data)
#         else:
#             return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        
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

'''

'''The HTML form should submit to the endpoint of the corresponding view.
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