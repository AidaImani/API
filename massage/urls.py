from django.urls import path
from . import views

urlpatterns = [
    path('chat/massage', views.Add_massage.as_view(), name='massage'),
    path('chat/conversation', views.Conversations.as_view(), name='conversation')
]
