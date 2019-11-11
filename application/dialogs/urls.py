from dialogs.views import messages_list
from django.urls import path

urlpatterns = [
    path('', messages_list, name='messages')
]
