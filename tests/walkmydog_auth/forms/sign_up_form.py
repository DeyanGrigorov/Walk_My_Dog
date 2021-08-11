from django.test import TestCase

from walk_my_dog.walkmydog_auth.forms import SignUpForm


class TestSignUpForm(TestCase):
    def test_empty_form(self):
        form = SignUpForm()
        form.full_clean()
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('email', form.fields)
        self.assertIn('city', form.fields)
        self.assertIn('category', form.fields)
        self.assertIn('password1', form.fields)
        self.assertIn('password2', form.fields)

    def test_is_invalid(self):
        form = SignUpForm(data={'email': 'test@abv.bg', "first_name": "test", "last_name": 'testov', 'city': 'Testovo',
                                'category': 'Dog owner', 'password1': 'azsxdc1234', 'password2': 'azsxdc1234'})
        self.assertFalse(form.is_valid())

    def test_form_is_valid(self):
        form = SignUpForm(data={'email': 'test@abv.bg', "first_name": "Test", "last_name": 'Testov', 'city': 'Testovo',
                                'category': 'Dog owner', 'password1': 'azsxdc1234', 'password2': 'azsxdc1234'})
        self.assertTrue(form.is_valid())
