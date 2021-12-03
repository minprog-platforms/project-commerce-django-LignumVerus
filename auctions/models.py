from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import related


class User(AbstractUser):
    pass

class Listing(models.Model):
    item_name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    start_bid = models.DecimalField(max_digits=8, decimal_places=2)
    photo_url = models.URLField(max_length=256)
    active = models.BooleanField(default=True)
    categories = models.TextField(max_length=256)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lister", blank=True)

class Comment(models.Model):
    desc = models.CharField(max_length=128)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenters", blank=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="comments")

class Bid(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidders", blank=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="bids")
