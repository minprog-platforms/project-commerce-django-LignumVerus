# Generated by Django 3.2.9 on 2021-12-01 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_alter_listing_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='commenters', to=settings.AUTH_USER_MODEL),
        ),
    ]
