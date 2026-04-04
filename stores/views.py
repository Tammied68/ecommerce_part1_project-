"""
Views for the stores application.

Provides functionality for vendors to create, edit, view, and delete stores,
and allows new users to register.
"""

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .models import Profile, Store


# -------------------------
# Store Views (Vendor Only)
# -------------------------

@login_required
def store_list(request):
    profile = getattr(request.user, "profile", None)

    # Buyers and admins should not access vendor dashboards
    if not profile or profile.role != "vendor":
        return redirect("/products/")

    stores = Store.objects.filter(vendor=request.user)
    return render(request, "stores/store_list.html", {"stores": stores})


@login_required
def create_store(request):
    profile = getattr(request.user, "profile", None)

    if not profile or profile.role != "vendor":
        messages.error(request, "Only vendors can create stores.")
        return redirect("/products/")

    if request.method == "POST":
        Store.objects.create(
            vendor=request.user,
            name=request.POST["name"],
            description=request.POST["description"],
        )
        return redirect("store_list")

    return render(request, "stores/create_store.html")


@login_required
def edit_store(request, store_id):
    profile = getattr(request.user, "profile", None)

    if not profile or profile.role != "vendor":
        return redirect("/products/")

    store = get_object_or_404(Store, id=store_id, vendor=request.user)

    if request.method == "POST":
        store.name = request.POST["name"]
        store.description = request.POST["description"]
        store.save()
        return redirect("store_list")

    return render(request, "stores/edit_store.html", {"store": store})


@login_required
def delete_store(request, store_id):
    profile = getattr(request.user, "profile", None)

    if not profile or profile.role != "vendor":
        return redirect("/products/")

    store = get_object_or_404(Store, id=store_id, vendor=request.user)

    if request.method == "POST":
        store.delete()
        return redirect("store_list")

    return render(request, "stores/delete_store.html", {"store": store})


# -------------------------
# Authentication Views
# -------------------------

def site_login(request):
    """
    Custom site login that blocks admin users from storefront access.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Admins must use Django admin
            if user.is_staff or user.is_superuser:
                messages.error(
                    request,
                    "Admins must log in through the admin panel."
                )
                return redirect("/admin/")

            login(request, user)
            return redirect("/products/")

        messages.error(request, "Invalid username or password.")

    return render(request, "registration/login.html")


def register(request):
    """
    Register a new user account, assign a role, and log the user in.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        role = request.POST.get("role")

        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, role=role)

            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("store_list")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})
