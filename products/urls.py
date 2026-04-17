from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.browse_products, name="list"),
    path("detail/<int:product_id>/", views.product_detail, name="product_detail"),
    path("review/<int:product_id>/", views.leave_review, name="leave_review"),
]
