import datetime

from django.core.validators import MinLengthValidator
from django.db import models
from petstagram.common.validators import (
    validate_file_max_size_in_mb,
    validate_only_letters,
)
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class Pet(models.Model):
    # Constants
    CAT = "Cat"
    DOG = "Dog"
    BUNNY = "Bunny"
    PARROT = "Parrot"
    FISH = "Fish"
    OTHER = "Other"
    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]
    NAME_MAX_LENGTH = 30

    # Fields(Columns)
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max(len(x) for x, _ in TYPES),
        choices=TYPES,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    # One-to-one relations

    # One-to-many relations
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    # Many-to-many relations

    # Properties

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    # Methods

    # Dunder methods

    # Meta
    class Meta:
        unique_together = ("user", "name")


class PetPhoto(models.Model):
    photo = models.ImageField(
        # validators=(validate_file_max_size_in_mb(5),),
        upload_to="images"
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        # validate at least one pet
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
