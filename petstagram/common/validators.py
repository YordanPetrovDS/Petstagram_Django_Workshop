from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_only_letters(value: str):
    for ch in value:
        if not ch.isalpha():
            # Invalid case
            raise ValidationError("Value must contains only letters")
    # valid case

    # if not all(ch.isalpha() for ch in value):
    #     raise ValidationError("Value must contains only letters")


def validate_file_max_size_in_mb(max_size):
    def validate(value):
        filesize = value.file.size
        if filesize > max_size * 1024**2:
            raise ValidationError(f"Max file size is {max_size} MB.")

    return validate


@deconstructible
class ValidateFileMaxSizeInMb:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        pass
