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


def user_game_easy(request):
    return render(request, 'game1.html')

def user_game_medium(request):
    return render(request, 'game2.html')

def user_game_difficult(request):
    return render(request, 'game3.html')

def user_profile(request):
    return render(request, 'profile.html')