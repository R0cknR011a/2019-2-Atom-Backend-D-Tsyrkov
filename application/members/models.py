from django.db import models
from chats.models import Chat
from dialogs.models import Message
from django.conf import settings

class Member(models.Model):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    chat_id = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    new_messages = models.TextField()
    last_read_message_id = models.OneToOneField(Message, on_delete=models.SET_NULL, null=True)
