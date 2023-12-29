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
   and the main app all the endpoint/logic
   related to render whole frontend pages
'''

'''  This will be the label of the endpoints: (Remember that the use of endpoint names is arbitrary. You just label in a way that 
is convinient for you)
Remember that all endpoint have before: http://127.0.0.1:8000/game/
Related to profile page:
profile/form/<pk>/  on profile all the form related to the particular user
profile/rating/<pk>/  on profile the rating related to the particular user
profile/score/<pk>/   on profile the score related to the particular user
profile/image/<pk>/   on profile the image related to the particular user

Note: It is everything selecting a single user and then particular fields and the
necessary methods.

Related to game page:
score/<pk>/    on game POST-PUT the score to the particular user (if user is auth only)
/image/<pk>/   on game GET the score to the particular user (if user is auth and has an 
image)

Related to sign up page:

sign_up/     on sign-up POST the form

Related to auth page:

log_in/     on log-in POST the form
log_out/ (I am not pretty sure about this one)

'''