# Generated by Django 3.2.9 on 2021-12-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20211201_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
