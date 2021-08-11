from django.test import TestCase

from walk_my_dog.profile_auth.forms import ProfileForm


class TestProfileForm(TestCase):
    def test_empty_form(self):
        form = ProfileForm()
        form.full_clean()
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('city', form.fields)
        self.assertIn('category', form.fields)
