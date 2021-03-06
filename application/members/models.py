from django.db import models
from chats.models import Chat
from dialogs.models import Message
from django.conf import settings

class Member(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True, verbose_name='Чат')
    new_messages = models.TextField(verbose_name='Новые сообщения', null=True, blank=True)
    last_read_message = models.OneToOneField(Message, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Последнее прочтённое сообщение')

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
