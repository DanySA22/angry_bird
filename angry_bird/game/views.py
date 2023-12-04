from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from .serializer import CustomerSerializer
 
# Create your views here.

def say_hello1(request):
    return render(request, 'game.html')
'''I should connect this to the easy field entry on the particular user object information.
Meaning that when user have easy in his level, the easy level page will be render.
It will look like this:
Create variable 1 that select level attribute entry data from the model Dificulty
for a particular user.
Create a condition: if variable 1 == easy render game/easy; if variable 1 == medium render game/medium
etc       
'''


def say_hello2(request):
    return render(request, 'game.html')

def say_hello3(request):
    return render(request, 'game.html')

#the next groups of views are for the frontend profile page that include Get, POST, PUT.
@api_view(['GET', 'POST', 'PUT'])
def user_profile(request):
    if request.method == 'GET':
        profile = Customer.objects.all()   # the ORM part; the data that I want to return. Check your frontend to see what particular data to return
        serializer = CustomerSerializer(profile, many=True) # the serializer class using as argument the ORM part. So transforming what data we decide to use on a Python dictionary.
        return Response(serializer.data)   # Transforming the resulting Python dictionary in a JSON object.
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data
            serializer.save()
            return Response('ok')
        else:
            return Response('de pinga esto')
        
    elif request.method == 'PUT':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data
            serializer.save()
            return Response('ok')
        else:
            return Response('de pinga esto')

#here either set it that each particular user data field match a 
#particular frontend field with the user info. That will be working all as a whole;
# or I set an endpoint and a function for each field which can give me more flexibility

@api_view()
def specific_user(request, pk):
    return Response(pk)


@api_view()
def game_score(request):
    puntuation = Customer.objects.all()
    serializer = CustomerSerializer(puntuation, many=True)
    return Response(serializer.data)  
    '''elif request.method == 'POST':
        return    
    elif request.method == 'PUT':
        return Response
    else:
        return ('Keep working on it')'''
    
         

''' in this function we should POST-PUT the score that a single user is cumuling while playing the game. 
 Then when user comeback to the game GET the last score. So
this function should be filter by user playing (id) and by the score field '''


@api_view(['GET', 'POST', 'PUT'])
def image_user(request):
    if request.method == 'GET':
        profile = Customer.objects.all()   # the ORM part; the data that I want to return. Check your frontend to see what particular data to return
        serializer = CustomerSerializer(profile, many=True) # the serializer class using as argument the ORM part. So transforming what data we decide to use on a Python dictionary.
        return Response(serializer.data)   # Transforming the resulting Python dictionary in a JSON object.
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data
            serializer.save()
            return Response('ok')
        else:
            return Response('de pinga esto')
        
    elif request.method == 'PUT':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data
            serializer.save()
            return Response('ok')
        else:
            return Response('de pinga esto')
    pass 
 
# in this function we GET the image field for that particular user. This
#on the game, profile and main pages. On profile it is also a POST

@api_view()
def sign_in_user(request):
    pass
#we set POST for collecting the user information

@api_view()
def auth_user(request):
    pass
#we set POST for auth the user. Validation rules could be included (on the back or frontend)


