from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('just_testing/', views.test_page),
    path('user_profile/', views.user_profile),
    path('user_game/', views.user_game)
    #path('level_select,', include)
]
