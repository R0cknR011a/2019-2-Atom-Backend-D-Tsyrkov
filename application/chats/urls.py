from chats.views import create_chat, get_all
from django.urls import path

urlpatterns = [
    path('create/', create_chat, name='create_chat'),
    path('get_all/', get_all, name='get_all'),
]
