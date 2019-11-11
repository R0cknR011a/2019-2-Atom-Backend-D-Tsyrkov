from users.views import search_username
from django.urls import path

urlpatterns = [
    path('username/<str:username>', search_username, name='search_name'),
]
