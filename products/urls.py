from django.urls import path
from . import views

urlpatterns = [
    # -------------------------
    # Buyer-facing routes
    # -------------------------
    path("", views.browse_products, name="browse_products"),
    path("detail/<int:product_id>/", views.product_detail, name="product_detail"),
    path("review/<int:product_id>/", views.leave_review, name="leave_review"),

    # -------------------------
    # Vendor routes (store-scoped)
    # -------------------------
    path("<int:store_id>/products/", views.list_store_products, name="list_store_products"),
    path("<int:store_id>/products/add/", views.add_product, name="add_product"),

    # -------------------------
    # Vendor routes (product-scoped)
    # -------------------------
    path("edit/<int:product_id>/", views.edit_product, name="edit_product"),
    path("delete/<int:product_id>/", views.delete_product, name="delete_product"),

    # -------------------------
    # Cart / checkout
    # -------------------------
    path("cart/", views.cart_view, name="cart_view"),
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("checkout/", views.checkout, name="checkout"),
]
