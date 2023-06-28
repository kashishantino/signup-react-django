from django.urls import path
from .views import *
urlpatterns = [
      # path('api/register/',RegisterAPI.as_view(),name='register'),
     path('sign_up/',SignupAPI.as_view()),
     path('login/',LoginAPI.as_view()),
     path('send/', Emailotp.as_view()),
    path('verify/', VerifyOTP.as_view()),
    
]
