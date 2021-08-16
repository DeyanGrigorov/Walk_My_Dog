from django.test import SimpleTestCase
from django.urls import reverse, resolve

from walk_my_dog.common.views import IndexView
from walk_my_dog.info.views import HowItWorksView
from walk_my_dog.profile_auth.views import update_profile, delete_profile
from walk_my_dog.profiles_render.views import list_profiles_owners, list_profiles_sitters, profile_details, \
    like_profile, SearchResultsView
from walk_my_dog.walkmydog_auth.views import sign_in_user, sign_out_user, SignUpView


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('landing page')
        self.assertEquals(resolve(url).func.view_class, IndexView)

    def test_info_url_is_resolved(self):
        url = reverse('how it works')
        self.assertEquals(resolve(url).func.view_class, HowItWorksView)

    def test_update_profile_url_is_resolved(self):
        url = reverse('update profile')
        self.assertEquals(resolve(url).func, update_profile)

    def test_delete_profile_url_is_resolved(self):
        url = reverse('delete profile')
        self.assertEquals(resolve(url).func, delete_profile)

    def test_list_profile_owners_url_is_resolved(self):
        url = reverse('list profiles owners')
        self.assertEquals(resolve(url).func, list_profiles_owners)

    def test_list_profile_sitters_url_is_resolved(self):
        url = reverse('list profiles sitters')
        self.assertEquals(resolve(url).func, list_profiles_sitters)

    def test_profile_details_url_is_resolved(self):
        url = reverse('list profile details', args=[1])
        self.assertEquals(resolve(url).func, profile_details)

    def test_profile_like_url_is_resolved(self):
        url = reverse('like profile', args=[1])
        self.assertEquals(resolve(url).func, like_profile)

    def test_sign_in_user_url_is_resolved(self):
        url = reverse('sign in user')
        self.assertEquals(resolve(url).func, sign_in_user)

    def test_sign_out_user_url_is_resolved(self):
        url = reverse('sign out user')
        self.assertEquals(resolve(url).func, sign_out_user)

    def test_sign_up_user_url_is_resolved(self):
        url = reverse('sign up user')
        self.assertEquals(resolve(url).func.view_class, SignUpView)

    def test_search_view_url_is_resolved(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func.view_class, SearchResultsView)
