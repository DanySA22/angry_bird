from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer
from .serializer import CustomerSerializer
from django.shortcuts import get_object_or_404 
 
# Create your views here.

#RELATED TO MAINPAGE

'''
A view that connect with each clickable level on the frontend. When the user click it create a
#Post in the related field and then when user populate his credentials we already have the dificulty level
# Create a condition: if variable 1 == easy render game/easy; if variable 1 == medium render game/medium
etc       
'''
class UserLevel(APIView):
    pass
def say_hello1(request):
    return render(request, 'game.html')


'''A View that GET user profile images if user isAuthenticated && uploaded a photo already otherwise 
just render the generic empty image (I should set that empty image as the default maybe)'''

class UserImage(APIView):
    pass

#RELATED TO GAMEPAGE (USER CAN ONLY ACCESS THIS PAGE IS AUTHENTICATED)

''' in this function we should POST-PUT the score that a single user is cumuling while playing the game. 
 Then when user comeback to the game GET the last score. So
this function should be filter by user playing (id) -OR JUST HAVING THE USER AUTHENTICATED AND WORKING
IN A SESSION - and by the score field.
The different elements involve in the frontend will use axios and they will interact with the same
endpoint but doing different methods each case'''


@api_view( ['GET', 'POST', 'PUT'])
def game_score(request, pk):
    puntuation = Customer.objects.get(pk=pk)
    serializer = CustomerSerializer(puntuation)
    return Response(serializer.data)  
    '''elif request.method == 'POST':
        return    
    elif request.method == 'PUT':
        return Response
    else:
        return ('Keep working on it')'''
        
        
'''A View that GET user profile images if user isAuthenticated && upload a photo already otherwise 
just render the generic empty image (I should set that empty image as the default maybe)'''

class UserImage(APIView):
    pass

#RELATED TO PROFILE PAGE (USER CAN ONLY ACCESS THIS PAGE IS AUTHENTICATED)

'''I should be able to GET (when user is authenticated already and load the page) the related user
information in the corresponding spaces: first name, last name, email, username, password, image, score, rating
I should also be able to POST-PUT this information. I will treat each html field independently, so 
each one will be a class (with the 3 methods already mentioned and related actions).
Or maybe there is a way to do it all in once through the session after auth maybe
'''
class UserFirstname(APIView):
    pass

class UserLastname(APIView):
    pass

class UserEmail(APIView):
    pass

class UserUsername(APIView):
    pass

class UserPassword(APIView):
    pass

class UserRating(APIView):
    pass

class UserImage(APIView):
    pass
    
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
    user = Customer.objects.get(pk=pk)
    serializer = CustomerSerializer(user)
    return Response(serializer.data)
'''The previous function is giving me the data for a particular user.
If I add a  filter to this I can select each particular field of this user data.'''



    
 #RELATED TO AUTHENTICATION PAGE
'''This will handle POST method of the form and get along with the auth process.
Validation rules could be included (on the back or frontend)'''

class UserAuthentication(APIView):
    pass


 
 #RELATED TO SIGN IN PAGE        

'''This will handle POST method of the form and get along with the auth process.
Validation rules could be included (on the back or frontend)'''

class UserSignin(APIView):
    pass







