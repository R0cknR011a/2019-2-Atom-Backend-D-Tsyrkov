# Generated by Django 2.2.5 on 2019-11-20 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_member_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='avatar',
        ),
    ]
