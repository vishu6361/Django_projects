# Generated by Django 2.1.5 on 2019-04-11 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='author',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
