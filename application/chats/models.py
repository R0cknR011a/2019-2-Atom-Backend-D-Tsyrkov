from django.db import models

class Chat(models.Model):
    is_group_chat = models.BooleanField(verbose_name='Групповой чат')
    topic = models.CharField(max_length=32, verbose_name='Топик')
    last_message = models.TextField(verbose_name='Последнее сообщение', null=True, blank=True)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
