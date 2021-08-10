from django.contrib.auth import get_user_model
from django.db import models


from walk_my_dog.profile_auth.models import Profile

UserModel = get_user_model()


class Like(models.Model):
    profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
