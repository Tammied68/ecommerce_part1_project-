from django.contrib import admin
from django.urls import include, path

from planning_app.views import home
from stores.views import site_login

urlpatterns = [
    # Home (must be the real landing page)
    path("", home, name="home"),

    # Admin
    path("admin/", admin.site.urls),

    # Custom storefront login (must be before auth.urls)
    path("accounts/login/", site_login, name="login"),

    # Django auth (logout, password reset, etc.)
    path("accounts/", include("django.contrib.auth.urls")),

    # Registration (your custom register view lives in stores.urls)
    path("accounts/", include("stores.urls")),

    # App routes
    path("stores/", include("stores.urls")),

    # ✅ IMPORTANT: register products with a namespace
    path("products/", include(("products.urls", "products"), namespace="products")),
]