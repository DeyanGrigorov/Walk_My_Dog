from django.urls import reverse

from tests.base.mixins import UserTestUtils, ProfileTestUtils
from tests.base.tests import WalkMyDogTestCase


class ProfileUpdateTest(WalkMyDogTestCase, UserTestUtils, ProfileTestUtils):
    def test_profile_expected_fields(self):
        user = self.create_user(email='deni@abv.bg', password='12345678', first_name='Deyan')

        expected_profile_title = f'{user.first_name}'
        expected_profile_email = f'{user.email}'
        self.assertEquals(expected_profile_title, 'Deyan')
        self.assertEquals(expected_profile_email, 'deni@abv.bg')

    def test_Update(self):
        user = self.create_user(email='deni@abv.bg', password='12345678', first_name='Deyan')
        user.first_name = "This has been changed"
        expected_profile_first_name = f'{user.first_name}'
        self.assertEquals(expected_profile_first_name, 'This has been changed')


