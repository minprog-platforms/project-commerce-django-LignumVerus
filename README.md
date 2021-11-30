
# eBait

This application is an online e-commerce auction site, where users
can post auction listings, place bids on listings and comment on
those listings.

## Getting Started
This application requires installing **django** using  
```pip3 install Django```.

## Design Document
The project consists of a few key pages that can be altered depending
on the certain conditions, like if the user is logged in or not or which
user is logged in. The HTML pages that are necessary are:

* Active listings page (index/home)
* Create listing page
* Listing page
* Register page
* Login page

### Pages
![UI_Sketch](/images/commercepages.png)
This image shows the different HTML pages that need to be made for
the site. Note that the content may change depending on the login
status and who is logged in.

### Workflow
![workflow](/images/commerceflowdiagram.png)
This image shows the application workflow. Since the active listings
page can always be reached from the navigation bar, just like the
register and login button (except when logged in), the arrows to
these using the navigation bar are omitted to improve clarity.
The dashed arrow shows how a new page is "added" to the other
listings (saved).

### Class Diagram
![models](/images/models.png)
This image shows a class diagram of the used models.
## Authors

- [Finn Peranovic](https://github.com/LignumVerus)


## Acknowledgements

This website was made for the minor "programmeren" at the
University of Amsterdam (2021-2022).