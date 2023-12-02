from django.shortcuts import render
from django.http import HttpResponse

 
# Create your views here.
def main_page(request):
    return render(request, 'mainpage.html')

def test_page(request):
    return render(request, 'index.html')

def user_profile(request):
    return render(request, 'profile.html')

def user_game(request):
    return render(request, 'game1.html')