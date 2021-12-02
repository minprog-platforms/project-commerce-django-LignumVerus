# Generated by Django 3.2.9 on 2021-11-30 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('desc', models.CharField(max_length=256)),
                ('start_bid', models.DecimalField(decimal_places=2, max_digits=8)),
                ('photo_url', models.URLField(max_length=256)),
                ('active', models.BooleanField()),
                ('categories', models.TextField(max_length=256)),
                ('bids', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.bid')),
                ('comments', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.comment')),
            ],
        ),
    ]
