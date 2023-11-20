from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_hello),
    path('profile/', views.user_profile),
    path('game_area/', views.game_score)
]
