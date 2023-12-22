from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('user_profile/', views.user_profile),
    path('user_game/easy/', views.user_game_easy),
    path('user_game/medium/', views.user_game_medium),
    path('user_game/difficult/', views.user_game_difficult),
    path('auth_game/', views.auth_game),
    path('sign_up_game/', views.sign_up_game)
    #path('level_select,', include)
]
