from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from .managers import WalkMyDogUserManager


class WalkMyDogUser(AbstractBaseUser, PermissionsMixin):
    CATEGORIES = (
        ('Dog walker', 'Dog walker'),
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

    # profile_image = models.ImageField(
    #     upload_to='profiles',
    #     null=True,
    #     blank=True,
    # )

    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    # is_dog_walker = models.BooleanField('I am dog walker', default=False)
    #
    # is_dog_owner = models.BooleanField('I am dog owner', default=False)

    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    objects = WalkMyDogUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['city', 'first_name', 'last_name']


class Profile(models.Model):
    user = models.OneToOneField(
        WalkMyDogUser,
        on_delete=models.CASCADE,
        primary_key=True,
        blank=True,
    )

    profile_image = models.ImageField(
        upload_to='profiles',
        null=True,
        blank=True,
    )

    first_name = models.CharField(max_length=30, blank=True)

    last_name = models.CharField(max_length=30, blank=True)

    city = models.CharField(max_length=50, blank=True)



from .signals import *
