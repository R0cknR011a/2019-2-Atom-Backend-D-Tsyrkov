from mainscreen.views import mainscreen
from django.urls import path

urlpatterns = [
    path('', mainscreen, name='mainscreeen')
]