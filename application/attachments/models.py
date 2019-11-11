from django.db import models
from chats.models import Chat
from dialogs.models import Message
from django.conf import settings

class Attachment(models.Model):
    chat_id = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True, verbose_name='Chat ID')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='User ID')
    message_id = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True, verbose_name='Message ID')
    attach_type = models.CharField(max_length=4, verbose_name='Attachment Type')
    url = models.CharField(max_length=128, verbose_name='URL')
