# Generated by Django 3.2.9 on 2021-12-01 09:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_listing_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='user',
            field=models.ManyToManyField(related_name='bidders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ManyToManyField(related_name='commenters', to=settings.AUTH_USER_MODEL),
        ),
    ]
