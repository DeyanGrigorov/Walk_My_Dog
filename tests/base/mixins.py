from django.contrib.auth import get_user_model

from walk_my_dog.profile_auth.models import Profile
from walk_my_dog.profiles_render.models import Like

UserModel = get_user_model()


class ProfileTestUtils:
    def create_profile(self, **kwargs):
        return Profile.objects.create(**kwargs)


class UserTestUtils:
    def create_user(self, **kwargs):
        return UserModel.objects.create_user(**kwargs)
