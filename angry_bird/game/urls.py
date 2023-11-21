from django.urls import path
from . import views

urlpatterns = [
    path('easy/', views.say_hello1),
    path('medium/', views.say_hello2),
    path('hard/', views.say_hello3),
    path('game_points/pk/', views.game_score),
    path('image_user/<pk>/', views.image_user),
    path('profile/', views.user_profile),
    path('profile/<pk>/', views.specific_user)
]

