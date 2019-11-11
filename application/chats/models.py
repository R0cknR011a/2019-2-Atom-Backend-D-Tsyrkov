from django.db import models

class Chat(models.Model):
    is_group_chat = models.BooleanField(verbose_name='Group chat status')
    topic = models.CharField(max_length=32, verbose_name='Topic')
    last_message = models.TextField(verbose_name='Last Message')
    
