from django.urls import path
from petstragram.main.views.generic import show_dashboard, show_home
from petstragram.main.views.pet_photos import (
    create_pet_photo,
    edit_pet_photo,
    like_pet_photo,
    show_pet_photo_details,
)
from petstragram.main.views.pets import create_pet, delete_pet, edit_pet
from petstragram.main.views.profiles import (
    create_profile,
    delete_profile,
    edit_profile,
    show_profile,
)

urlpatterns = (
    path("", show_home, name="index"),
    path("dashboard/", show_dashboard, name="dashboard"),
    path("profile/", show_profile, name="profile details"),
    path("profile/create/", create_profile, name="create profile"),
    path("profile/edit/", edit_profile, name="edit profile"),
    path("profile/delete/", delete_profile, name="delete profile"),
    path(
        "photo/details/<int:pk>/",
        show_pet_photo_details,
        name="pet photo details",
    ),
    path("photo/add/", create_pet_photo, name="create pet photo"),
    path("photo/edit/<int:pk>/", edit_pet_photo, name="edit pet photo"),
    path("photo/like/<int:pk>/", like_pet_photo, name="like pet photo"),
    path("pet/add/", create_pet, name="create pet"),
    path("pet/edit/<int:pk>/", edit_pet, name="edit pet"),
    path("pet/delete/<int:pk>/", delete_pet, name="delete pet"),
)
