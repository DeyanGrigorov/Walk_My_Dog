from django.urls import path

from walk_my_dog.walkmydog_auth.views import sign_in_user, sign_out_user, sign_up_user

urlpatterns = (
    path('signin/', sign_in_user, name='sign in user'),
    path('signout/', sign_out_user, name='sign out user'),
    path('signup/', sign_up_user, name='sign up user'),
    )
