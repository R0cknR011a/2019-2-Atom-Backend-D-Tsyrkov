from django.db import models
from chats.models import Chat
from django.conf import settings

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True, verbose_name='Чат')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    content = models.TextField(verbose_name='Контент')
    added_at = models.DateTimeField(verbose_name='Контент')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
