from members.views import members_list
from django.urls import path

urlpatterns = [
    path('', members_list, name='members')
]
