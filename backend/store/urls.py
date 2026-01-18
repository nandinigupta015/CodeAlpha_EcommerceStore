from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("cart/", views.cart, name="cart"),
    path("add-to-cart/<int:pk>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:pk>/", views.remove_from_cart, name="remove_from_cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("register/", views.register, name="register"),
    path("increase/<int:pk>/", views.increase_quantity, name="increase_quantity"),
    path("decrease/<int:pk>/", views.decrease_quantity, name="decrease_quantity"),
    path("my-orders/", views.my_orders, name="my_orders"),
    path("profile/", views.profile, name="profile"),


]

