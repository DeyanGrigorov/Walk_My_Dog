from django.urls import path


from walk_my_dog.profiles_render.views import list_profiles_owners, list_profiles_sitters, profile_details

urlpatterns = (
    path('profiles-owners/', list_profiles_owners, name='list profiles owners'),
    path('profiles-sitters/', list_profiles_sitters, name='list profiles sitters'),
    path('profile-details/<int:pk>', profile_details, name='list profile details'),

)
