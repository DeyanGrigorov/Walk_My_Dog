from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User
from django.core.exceptions import ValidationError
from django.db import models

from .managers import WalkMyDogUserManager


def validate_capitalized(value):
    if value != value.capitalize():
        raise ValidationError(f'Field: {value} first letter must be capital.',
                              code='invalid',
                              params={'value': value})


class WalkMyDogUser(AbstractBaseUser, PermissionsMixin):
    CATEGORIES = (
        ('Dog sitter', 'Dog sitter'),
        ('Dog owner', 'Dog owner'),
    )

    category = models.CharField(max_length=50, choices=CATEGORIES)

    first_name = models.CharField(
        max_length=12,
        validators=[validate_capitalized],
    )

    last_name = models.CharField(
        max_length=13,
        validators=[validate_capitalized],
    )

    city = models.CharField(
        max_length=50,
        validators=[validate_capitalized],
    )

    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    objects = WalkMyDogUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'category', ]
