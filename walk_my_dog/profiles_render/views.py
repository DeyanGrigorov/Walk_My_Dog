from django.shortcuts import render

from walk_my_dog.profile_auth.models import Profile
from walk_my_dog.walkmydog_auth.models import WalkMyDogUser


def list_profiles_owners(request):
    # all_profiles = Profile.objects.all()
    dog_owners = Profile.objects.filter(category='Dog owner')
    # dog_walkers = Profile.objects.filter(category='Dog walker')

    context = {
        'DogOwner': dog_owners,
     }

    return render(request, 'profiles/list_profiles_owners.html', context)


def list_profiles_walkers(request):
    dog_sitters = Profile.objects.filter(category='Dog walker')

    context = {
        'DogSitter': dog_sitters,
    }

    return render(request, 'profiles/list_profiles_sitters.html', context)
