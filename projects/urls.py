from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.product_index, name="product_index"),
    path("products/<int:pk>/", views.product_detail, name="product_detail"),
    path("cart/", views.cart, name="cart"),
    path("cart/<int:pk>", views.add_to_cart, name="add_to_cart"),
    path("cart/save", views.save_cart, name="save_cart"),
    path("cart/delete/<int:pk>", views.cart_delete, name="cart_delete")
]