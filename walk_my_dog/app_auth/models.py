from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.
from walk_my_dog.app_auth.managers import WalkMyDogUserManager


class WalkMyDogUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = WalkMyDogUserManager()


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
