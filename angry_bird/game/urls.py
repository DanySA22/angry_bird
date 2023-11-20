from django.urls import path
from . import views

urlpatterns = [
    path('easy/', views.say_hello1),
    path('medium/', views.say_hello2),
    path('hard/', views.say_hello3),
    #this 3 will render the different game pages 
    # and their difficulties.
    path('game_area/', views.game_score),
    path('profile/', views.user_profile),
    path('profile/<pk>/', views.specific_user)
]

