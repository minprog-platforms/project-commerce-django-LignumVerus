# Generated by Django 3.2.9 on 2021-12-01 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20211201_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='bids',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='comments',
        ),
        migrations.AddField(
            model_name='bid',
            name='listing',
            field=models.ManyToManyField(blank=True, related_name='bids', to='auctions.Listing'),
        ),
        migrations.AddField(
            model_name='comment',
            name='listing',
            field=models.ManyToManyField(blank=True, related_name='comments', to='auctions.Listing'),
        ),
    ]