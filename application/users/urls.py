from users.views import search_username, get_all, create
from django.urls import path

urlpatterns = [
    path('search_username/', search_username, name='search_name'),
    path('get_all/', get_all, name='get_all'),
    path('create/', create, name='create'),
]
