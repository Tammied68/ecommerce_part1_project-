from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

from stores.views import site_login

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # ✅ Custom storefront login (MUST be before auth.urls)
    path("accounts/login/", site_login, name="login"),

    # Django auth (logout, password reset, etc.)
    path("accounts/", include("django.contrib.auth.urls")),

    # Registration
    path("accounts/", include("stores.urls")),

    # App routes
    path("stores/", include("stores.urls")),
    path("products/", include("products.urls")),

    # Default route
    path("", lambda request: redirect("/products/")),
]