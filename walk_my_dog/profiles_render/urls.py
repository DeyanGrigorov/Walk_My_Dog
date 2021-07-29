from django.urls import path


from walk_my_dog.profiles_render.views import list_profiles_owners, list_profiles_walkers, profile_details

urlpatterns = (
    path('profiles-owners/', list_profiles_owners, name='list profiles owners'),
    path('profiles-sitters/', list_profiles_walkers, name='list profiles sitters'),
    path('profile-details/<int:pk>', profile_details, name='list profile details'),

)
