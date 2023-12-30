from django.urls import path
from . import views

urlpatterns = [
    path('score/', views.ScoreSave.as_view()),
    path('profile/score/', views.UserScore.as_view()),
    path('profile/form/', views.FormProfile.as_view()),
    path('profile/rating/', views.UserRating.as_view()),
    path('sign_up/', views.UserSignin.as_view()),
    path('log_in/', views.UserAuthentication.as_view()),
    path('log_out/', views.UserLogout.as_view()),
    # path('media1/', views.image_user),
    # path('profile/image/<pk>/', views.UserImageProfile.as_view()),
    # path('image/', views.UserImage.as_view()),
]

''' I will let the game app handle all the endpoints and apis
   related to specific elements
   and the main1 app all the endpoint/logic
   related to render whole frontend pages
'''

