from dialogs.views import get_all, create, read_message 
from django.urls import path

urlpatterns = [
    path('get_all/', get_all, name='get_all'),
    path('create/', create, name='create'),
    path('read_message/', read_message, name='read_message'),
]
