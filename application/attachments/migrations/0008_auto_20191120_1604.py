# Generated by Django 2.2.5 on 2019-11-20 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0007_attachment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='content',
            field=models.ImageField(null=True, upload_to='attachments/'),
        ),
    ]