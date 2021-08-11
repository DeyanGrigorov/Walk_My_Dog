from django.contrib.auth import get_user_model

from tests.base.tests import WalkMyDogTestCase

UserModel = get_user_model()


class LogInTest(WalkMyDogTestCase):
    def test_IsUserLoggedIn(self):
        self.client.force_login(self.user)

        self.assertEqual(int(self.client.session['_auth_user_id']), self.user.pk)

        self.assertIn('_auth_user_id', self.client.session)
