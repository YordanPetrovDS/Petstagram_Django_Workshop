import datetime

from django import forms
from petstagram.common.helpers import (
    BootstrapFormMixin,
    DisabledFieldsFormMixin,
)
from petstagram.main.models import Pet, PetPhoto

now = datetime.datetime.now()
CURRENT_DATE = f"{now.year}-{now.month:02d}-{now.day:02d}"


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        pet = super().save(commit=False)

        pet.user = self.user
        if commit:
            pet.save()

        return pet

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
