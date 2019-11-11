from django.db import models
from chats.models import Chat
from django.conf import settings

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True, verbose_name='Chat')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    added_at = models.DateTimeField()
