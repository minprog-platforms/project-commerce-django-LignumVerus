# Generated by Django 3.2.9 on 2021-12-01 08:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20211201_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='user',
        ),
        migrations.AddField(
            model_name='bid',
            name='user',
            field=models.ManyToManyField(related_name='bidders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ManyToManyField(related_name='commenters', to=settings.AUTH_USER_MODEL),
        ),
    ]
