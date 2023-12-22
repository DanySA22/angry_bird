from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer
from .serializer import CustomerSerializer
from django.shortcuts import get_object_or_404 
 
# Create your views here.

#RELATED TO GAMEPAGE

''' in this function we should POST-PUT the score that a single user cumulate before he lose.
This means that when user lose not only we will see that pop-up with Game over and the score
but this score will be POST/PUT on user instance DB. When user check in profile will see
that last POST/PUT of the score. If user is playing without being auth, this info will not be saved.
So this POST/PUT only work if isAuthenticated. 
 So this function should be filter by user playing (id) -OR JUST HAVING THE USER AUTHENTICATED AND WORKING
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
        
        
'''A View that GET user profile images if user isAuthenticated && uploaded a photo already otherwise 
just render the generic empty image (I set that empty image as the default which
is also the one that appears on Anonymus users)'''

class UserImage(APIView):
    pass

#RELATED TO PROFILE PAGE (USER CAN ONLY ACCESS THIS PAGE IF IT IS AUTHENTICATED)

'''I should be able to GET the related user information in the corresponding spaces: 
first name, last name, email, username, password, image.
I should also be able to POST-PUT those informations. Rating will not have GET only 
POST-PUT.  Score only have GET.
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

class UserImage(APIView):
    pass

class UserScore(APIView):
    pass

class UserRating(APIView):
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
difficulty and just handlesd with frontend endpoint redirection:
Eliminated the level model and relationship; eliminate the class related to level 
handling
    
'''
 
 #RELATED TO SIGN UP PAGE        

'''This will handle POST method of the form. Validation rules could be included (on the back or frontend).
After completion user will be redirected to auth page. Which means that when user
click submit a POST will happend to the backend -if valid the form- and a redirection will happen to
auth endpoint -this is with a JS async promise (On Axios): after POST then redirect to auth endpoint '''

class UserSignin(APIView):
    pass

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

class UserAuthentication(APIView):
    pass






