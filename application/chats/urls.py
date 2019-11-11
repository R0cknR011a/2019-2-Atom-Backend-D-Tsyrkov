from chats.views import alena_chat, anton_chat, create_chat, get_all
from django.urls import path

urlpatterns = [
    path('create/<int:is_group_chat>/<str:topic>/<str:last_message>/', create_chat, name='create_chat'),
    path('all/', get_all, name='get_all'),
]
