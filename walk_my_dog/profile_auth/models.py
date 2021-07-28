from django.db import models

from ..walkmydog_auth.models import WalkMyDogUser


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

    category = models.CharField(max_length=50)


from .signals import *
