from dialogs.views import get_all, create, messages_with 
from django.urls import path

urlpatterns = [
    path('get_all/', get_all, name='get_all'),
    path('create/', create, name='create'),
    path('messages_with/', messages_with, name='messages_with'),
]
