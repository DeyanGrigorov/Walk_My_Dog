from django.test import TestCase

from tests.base.mixins import UserTestUtils
from tests.base.tests import WalkMyDogTestCase
from walk_my_dog.profile_auth.forms import ProfileForm


class TestProfileForm(WalkMyDogTestCase,UserTestUtils):
    def test_empty_form(self):
        form = ProfileForm()
        form.full_clean()
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('city', form.fields)
        self.assertIn('category', form.fields)
        self.assertIn('age', form.fields)
        self.assertIn('text', form.fields)
        self.assertIn('phone_number', form.fields)
        self.assertIn('profile_image', form.fields)
