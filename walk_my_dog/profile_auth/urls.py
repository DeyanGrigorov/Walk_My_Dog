from django.urls import path

from walk_my_dog.profile_auth.views import update_profile, delete_profile

urlpatterns = (
    path('profile/', update_profile, name='update profile'),
    path('delete_profile/', delete_profile, name='delete profile'),

)
