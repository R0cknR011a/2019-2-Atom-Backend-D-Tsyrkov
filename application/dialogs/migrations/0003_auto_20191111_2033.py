# Generated by Django 2.2.5 on 2019-11-11 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
        ('dialogs', '0002_message_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='chat_id',
        ),
        migrations.AddField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chats.Chat', verbose_name='Chat'),
        ),
    ]