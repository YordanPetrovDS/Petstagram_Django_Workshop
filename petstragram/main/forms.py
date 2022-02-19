import datetime

from django import forms
from petstragram.main.helpers import (
    BootstrapFormMixin,
    DisabledFieldsFormMixin,
)
from petstragram.main.models import Pet, PetPhoto, Profile

now = datetime.datetime.now()
CURRENT_DATE = f"{now.year}-{now.month:02d}-{now.day:02d}"


class CreateProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "picture")
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter first name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter last name",
                }
            ),
            "picture": forms.TextInput(
                attrs={
                    "placeholder": "Enter URL",
                }
            ),
        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial["gender"] = Profile.DO_NOT_SHOW

    class Meta:
        model = Profile
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter first name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter last name",
                }
            ),
            "picture": forms.TextInput(
                attrs={
                    "placeholder": "Enter URL",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter email",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Enter description",
                    "rows": 3,
                }
            ),
            "date_of_birth": forms.DateInput(
                attrs={
                    "min": "1920-01-01",
                    "max": CURRENT_DATE,
                    "type": "date",
                }
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        pets = list(self.instance.pet_set.all())
        PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet
        fields = ("name", "type", "date_of_birth")
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter pet name",
                }
            ),
            "date_of_birth": forms.DateInput(
                attrs={
                    "min": "1920-01-01",
                    "max": CURRENT_DATE,
                    "type": "date",
                }
            ),
        }


class EditPetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet
        exclude = ("user_profile",)
        widgets = {
            "date_of_birth": forms.DateInput(
                attrs={
                    "min": "1920-01-01",
                    "max": CURRENT_DATE,
                    "type": "date",
                }
            ),
        }


class DeletePetForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):

    # disabled_fields = ("name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        exclude = ("user_profile",)
