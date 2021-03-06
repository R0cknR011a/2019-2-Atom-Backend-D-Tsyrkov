from django.db import models
from chats.models import Chat
from dialogs.models import Message
from django.conf import settings

class Attachment(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True, verbose_name='Чат')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пользователь')
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Сообщение')
    attach_type = models.CharField(max_length=32, verbose_name='Тип', blank=True, null=True)
    url = models.CharField(max_length=128, verbose_name='Адрес', blank=True, null=True)

    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'
