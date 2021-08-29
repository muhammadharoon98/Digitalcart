from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="About"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:id>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("shop/dashboard/", views.admin, name="Dashboard"),
    path("shop/dashboard/calendar/", views.calendar, name="Calendar"),
    path("shop/dashboard/forms/", views.forms, name="Forms"),
    path("shop/dashboard/icons/", views.icons, name="Icons"),
    path("shop/dashboard/login/", views.login, name="Login"),
    path("shop/dashboard/profile/", views.profile, name="Profile"),
    path("shop/dashboard/register/", views.register, name="Register"),
    path("shop/dashboard/reset_password/", views.reset_password, name="Reset_Password"),
    path("shop/dashboard/tables/", views.tables, name="Tables"),
]
