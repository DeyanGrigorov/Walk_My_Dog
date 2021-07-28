from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User
from django.db import models

from .managers import WalkMyDogUserManager


class WalkMyDogUser(AbstractBaseUser, PermissionsMixin):
    CATEGORIES = (
        ('Dog sitter', 'Dog sitter'),
        ('Dog owner', 'Dog owner'),
    )

    category = models.CharField(max_length=50, choices=CATEGORIES)

    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
    )

    city = models.CharField(
        max_length=50,
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
    REQUIRED_FIELDS = ['city', 'first_name', 'last_name', ]


