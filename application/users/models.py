from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.CharField(default="avatars/defaultAvatar", null=True, blank=True, max_length=32)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
