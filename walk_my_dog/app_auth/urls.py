from django.urls import path

from walk_my_dog.app_auth.views import test

urlpatterns = (
    path('', test, name='test_view'),
    )
