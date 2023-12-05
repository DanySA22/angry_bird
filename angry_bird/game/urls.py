from django.urls import path
from . import views

urlpatterns = [
    path('easy/', views.say_hello1),
    path('medium/', views.say_hello2),
    path('hard/', views.say_hello3),
    path('game_points/', views.game_score),
    path('media1/', views.image_user),
    path('profile/', views.user_profile),
    path('profile/<pk>/', views.specific_user)
]

''' I will let the game app handle all the endpoints and apis
   related to specific elements
   and the main app all the endpoint/logic
   related to render whole frontend pages
'''