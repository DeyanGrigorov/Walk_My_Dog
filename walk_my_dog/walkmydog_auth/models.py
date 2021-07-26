from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from .managers import WalkMyDogUserManager


class WalkMyDogUser(AbstractBaseUser, PermissionsMixin):
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

    is_dog_walker = models.BooleanField('dog walker status', default=False)

    is_dog_owner = models.BooleanField('dog owner status', default=False)

    date_created = models.DateTimeField(
        auto_now_add=True,
    )



    objects = WalkMyDogUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['city', 'is_dog_owner', 'is_dog_walker', 'first_name', 'last_name']


class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to='profiles'
    )

    user = models.OneToOneField(
        WalkMyDogUser,
        on_delete=models.CASCADE,
        primary_key=True,
        blank=True,
    )


from .signals import *
