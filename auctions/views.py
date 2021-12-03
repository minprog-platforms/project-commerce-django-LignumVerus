from typing import List
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.forms.fields import URLField
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Bid, Comment


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


class NewListingForm(forms.ModelForm):
    categories = forms.CharField(strip=True,
                                 widget=forms.Textarea)
    desc = forms.CharField(strip=True,
                           widget=forms.Textarea,
                           label="description")
    photo_url = forms.URLField(required=False)
    
    class Meta:
        model = Listing
        fields = ['item_name', 'desc', 'start_bid', 'photo_url', 'categories']
        labels = {
            "item_name": "item name",
            "start_bid": "starting bid",
            "photo_url": "photo URL"
        }


@login_required
def new_listing(request):
    if request.method == "POST":

        form = NewListingForm(request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.user = request.user
            new_entry.save()

            id = new_entry.id

            return HttpResponseRedirect(f"listing/{id}")

    return render(request, "auctions/new_listing.html", {
        "form": NewListingForm()
    })


class NewBidForm(forms.ModelForm):
    price = forms.DecimalField(label="Place a bid:")
    
    class Meta:
        model = Bid
        exclude = ["user", "listing"]


class NewCommentForm(forms.ModelForm):
    desc = forms.CharField(strip=True,
                           widget=forms.Textarea(attrs={'rows':2, 'cols':1}),
                           label="Place a comment:")

    class Meta:
        model = Comment
        exclude = ["user", "listing"]


def listing(request, listing_id):
    listing_id = int(listing_id)
    listing = Listing.objects.get(id=listing_id)

    if request.method == "POST" and "place_bid" in request.POST:
        bid_form = NewBidForm(request.POST)

        if bid_form.is_valid():
            new_entry = bid_form.save(commit=False)
            new_entry.user = request.user
            new_entry.listing = listing

            # first, check if any input was invalid and show an error when it is
            start_bid = new_entry.listing.start_bid
            new_bid = new_entry.price

            # gets old bid (second highest) if there are multiple bids
            try:
                old_bid = Bid.objects.filter(listing=listing_id).last().price
                print(f"FIRST TRY BLOCK {old_bid}")
            except Exception:
                old_bid = start_bid
                print(f"LAST EXCEPTION BLOCK {old_bid}")

            # if input was valid, save the new entry.
            if start_bid == old_bid and Bid.objects.filter(listing=listing_id).count() == 0:
                if new_bid >= old_bid:
                    new_entry.save()
                    messages.success(request, 'Your bid was placed successfully!')
                else:
                    messages.warning(request, "Your bid must be higher than or equal to the starting bid")
            elif new_bid > start_bid and new_bid > old_bid:
                new_entry.save()
                messages.success(request, "Your bid was placed successfully!")
            else:
                messages.warning(request, "Your bid must be higher than the previous bid")

            return render(request, "auctions/listing.html", {
                "listing_id": listing_id,
                "listing": listing,
                "bid_form": NewBidForm(),
                "new_bid": new_bid,
                "start_bid": start_bid,
                "old_bid": old_bid,
                "comment_form": NewCommentForm(),
                "comments": Comment.objects.filter(listing=listing_id)
                })
    if request.method == "POST" and "place_comment" in request.POST:
        comment_form = NewCommentForm(request.POST)

        if comment_form.is_valid():
            new_entry = comment_form.save(commit=False)
            new_entry.user = request.user
            print(new_entry.user.username)

            new_entry.listing = listing
            print(new_entry.listing.id)
            new_entry.save()

            return render(request, "auctions/listing.html", {
                "listing_id": listing_id,
                "listing": listing,
                "bid_form": NewBidForm(),
                "comment_form": NewCommentForm(),
                "comments": Comment.objects.filter(listing=listing_id)
                })

    # button that closes listing
    if request.method == "POST" and "close_auction" in request.POST:
        listing.active = False
        listing.save()

    return render(request, "auctions/listing.html", {
        "listing_id": listing_id,
        "listing": Listing.objects.get(id=listing_id),
        "bid_form": NewBidForm(),
        "comment_form": NewCommentForm(),
        "comments": Comment.objects.filter(listing=listing_id)
    })
