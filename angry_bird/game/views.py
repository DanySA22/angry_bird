from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from .serializer import CustomerSerializer
 
# Create your views here.

def say_hello1(request):
    return render(request, 'game.html')

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

@api_view()
def specific_user(request, pk):
    return Response(pk)

#the next groups of views are for the frontend main page that include Get (rendering the HTML).



#the next groups of views are for the frontend sign in page that include Get (rendering the HTML), POST(data).
#the next groups of views are for the frontend game page that include Get and rendering 3 different endpoint for each level of dificulty).

@api_view()
def game_score(request):
    # puntuation = Customer.objects.filter(username)
    #serializer = CustomerSerializer(puntuation)
    #return Response(serializer.data)  
    return Response('todo bien')
