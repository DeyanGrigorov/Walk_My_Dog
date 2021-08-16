from django.test import TestCase
from django.urls import resolve, reverse

from walk_my_dog.common.views import IndexView


class LandingPageTest(TestCase):

    def test_root_url_resolves_to_landing_page_view(self):
        found = resolve('/')
        url = reverse('landing page')
        resp = self.client.get(url)
        self.assertEqual(found.func.view_class, IndexView)
        self.assertEqual(resp.status_code, 200)

    def test_landing_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<title>Walk My Dog</title>')

    def test_landing_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')
