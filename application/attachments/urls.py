from attachments.views import get_all, create, upload_file
from django.urls import path

urlpatterns = [
    path('get_all/', get_all, name='get_all'),
    path('create/', create, name='create'),
    path('upload_file/', upload_file, name='upload_file'),
]
