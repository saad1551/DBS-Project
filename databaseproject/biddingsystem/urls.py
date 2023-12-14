from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("listing/<str:listing_id>", views.listing, name="listing"),
    path("login", views.log_in, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.log_out, name="logout")
]