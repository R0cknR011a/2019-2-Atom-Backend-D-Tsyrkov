from members.views import get_all, create
from django.urls import path

urlpatterns = [
    path('create/', create, name='create'),
    path('get_all/', get_all, name='get_all'),
]
