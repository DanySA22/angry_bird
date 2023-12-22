from django.urls import path
from . import views

urlpatterns = [
    path('game_points/<pk>/', views.game_score),
    path('profile/', views.user_profile),
    path('profile/<pk>/', views.specific_user),
    # path('media1/', views.image_user),
]

''' I will let the game app handle all the endpoints and apis
   related to specific elements
   and the main app all the endpoint/logic
   related to render whole frontend pages
'''

'''  This will be the label of the endpoints: (Remember that the use of endpoint names is arbitrary. You just label in a way that 
is convinient for you)

'''