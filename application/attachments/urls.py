from attachments.views import attachments_list
from django.urls import path

urlpatterns = [
    path('', attachments_list, name='attachments')
]
