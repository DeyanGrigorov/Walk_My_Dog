from django.urls import reverse

from tests.base.tests import WalkMyDogTestCase


class ProfileDetailsTest(WalkMyDogTestCase):

    def test_getDetails_whenLoggedInUser_UserShouldGetDetails(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('list profile details', args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user.id, response.context['profile'].user_id)

