from attachments.views import get_all, create
from django.urls import path

urlpatterns = [
    path('get_all/', get_all, name='get_all'),
    path('create/', create, name='create'),
]
