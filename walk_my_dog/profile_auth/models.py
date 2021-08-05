from django.db import models

from ..walkmydog_auth.models import WalkMyDogUser
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
        blank=True,
    )

    profile_image = models.ImageField(
        upload_to='profiles',
        null=True,
        blank=True,
    )
    age = models.IntegerField(blank=True, null=True)

    phone_number = models.IntegerField(blank=True, null=True)

    first_name = models.CharField(max_length=12, blank=True)

    last_name = models.CharField(max_length=13, blank=True)

    city = models.CharField(max_length=50, blank=True, null=True)

    category = models.CharField(max_length=50)

    text = models.TextField(max_length=255, blank=True, null=True)


from .signals import *
