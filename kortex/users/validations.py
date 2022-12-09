from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image


def validate_first_name(name:str) -> None:
    if len(name) < 3:
        raise ValidationError("First name too small")

def validate_last_name(name:str) -> None:
    if len(name) < 3:
        raise ValidationError("Last name too small")

