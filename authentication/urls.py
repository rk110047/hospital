from django.urls import path
from .views import RegisterAPIView,LoginWithTokenAuthenticationAPIView,PasswordChangeAPIView,SubUserListCreateAPIView



urlpatterns=[
    path('login/token/',LoginWithTokenAuthenticationAPIView.as_view(),name='login for token'),
    path('register/',RegisterAPIView.as_view(),name='register'),
    path('change-password/',PasswordChangeAPIView.as_view(),name='change password'),
    path('subusers/LC/',SubUserListCreateAPIView.as_view(),name='sub-user-lc'),



]
