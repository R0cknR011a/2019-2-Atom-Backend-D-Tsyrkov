from chat_list.views import rick, morty
from django.urls import path

urlpatterns = [
    path('rick/', rick, name='rick'),
    path('morty/', morty, name='morty'),
]
