from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("listing/<str:listing_id>", views.listing, name="listing"),
    path("login", views.log_in, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.log_out, name="logout"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("payment/<str:listing_id>", views.payment, name="payment"),
    path("watchlist", views.watchlist, name="watchlist"),

    #API routes
    path("follow", views.follow, name="follow")
]