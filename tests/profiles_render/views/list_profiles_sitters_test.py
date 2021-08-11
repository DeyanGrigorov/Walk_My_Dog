from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

from tests.base.tests import WalkMyDogTestCase


UserModel = get_user_model()


class ProfileOwnersList(WalkMyDogTestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='deian@abv.bg', password='123456', category='Dog sitter')

    def test_getOwnersList_whenLoggedInUser_ShouldSeeListDetailsOwners(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('list profiles sitters'))

        profiles = list(response.context['page'])

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(profiles, list(response.context['profiles']))


