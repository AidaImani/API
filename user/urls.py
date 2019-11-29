from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.Signup.as_view(), name='signup'),
    path('login', views.Login.as_view(), name='login'),
    path('profile', views.Profile.as_view(), name='profile'),
    path('userList', views.List_of_user.as_view(), name='userList')

]
