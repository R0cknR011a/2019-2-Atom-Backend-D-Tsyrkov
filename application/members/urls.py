from members.views import get_all, create, add_chat
from django.urls import path

urlpatterns = [
    path('create/', create, name='create'),
    path('get_all/', get_all, name='get_all'),
    path('add_chat/', add_chat, name='add_chat'),
]
