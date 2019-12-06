from users.views import search_username, get_all, create, get_settings, set_settings, set_avatar
from django.urls import path

urlpatterns = [
    path('search_username/', search_username, name='search_name'),
    path('get_all/', get_all, name='get_all'),
    path('create/', create, name='create'),
    path('get_settings/', get_settings, name="get_settings"),
    path('set_settings/', set_settings, name="set_settings"),
    path('set_avatar/', set_avatar, name="set_avatar"),
]
