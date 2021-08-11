from django.urls import reverse

from tests.base.mixins import ProfileTestUtils, UserTestUtils
from tests.base.tests import WalkMyDogTestCase
from walk_my_dog.profiles_render.models import Like


class LikeTest(WalkMyDogTestCase, ProfileTestUtils, UserTestUtils):

    def test_UserIsAlreadyLiked(self):
        self.client.force_login(self.user)
        profile_user = self.create_user(email='deni@abv.bg', password='12345678')

        instance = profile_user.profile
        like = Like.objects.create(
            profile=instance,
            user=self.user
        )

        response = self.client.get(reverse('list profile details', kwargs={'pk': profile_user.id}))

        self.assertTrue(response.context['is_liked'])

    def test_UserIsNotLiked(self):
        self.client.force_login(self.user)
        profile_user = self.create_user(email='deni@abv.bg', password='12345678')

        response = self.client.get(reverse('list profile details', kwargs={'pk': profile_user.id}))

        self.assertFalse(response.context['is_liked'])
