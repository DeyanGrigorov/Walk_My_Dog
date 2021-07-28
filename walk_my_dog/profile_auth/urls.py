from django.urls import path

from walk_my_dog.profile_auth.views import update_profile

urlpatterns = (
    path('profile/', update_profile, name='update profile'),

)
