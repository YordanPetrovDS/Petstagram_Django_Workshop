from django.contrib import admin
from petstragram.main.models import Pet, Profile, PetPhoto


class PetInlineAdmin(admin.StackedInline):
    model = Pet


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = (PetInlineAdmin,)
    list_display = ("first_name", "last_name")


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "type")


@admin.register(PetPhoto)
class PetPhoto(admin.ModelAdmin):
    pass
