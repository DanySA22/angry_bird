from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

# Create your views here. Change all this view to class based views later.
def main_page(request):
    return render(request, 'mainpage.html')

def auth_game(request):
    return render(request, 'authpage.html')

def sign_up_game(request):
    return render(request, 'signinpage.html')


# @api_view(['GET'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])

def user_game_easy(request):
    return render(request, 'game1.html')

def user_game_medium(request):
    return render(request, 'game2.html')

def user_game_difficult(request):
    return render(request, 'game3.html')


''' This view set it to only work when user is authenticated; 
the other can work with anonymus user and the images profile set just take
the default value -the empty profile that is already set-'''
def user_profile(request):
    return render(request, 'profile.html')