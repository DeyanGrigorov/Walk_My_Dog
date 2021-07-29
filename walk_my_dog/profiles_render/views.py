from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from walk_my_dog.profile_auth.models import Profile


def list_profiles_owners(request):
    dog_owners = Profile.objects.filter(category='Dog owner')

    context = {
        'DogOwner': dog_owners,
    }

    return render(request, 'profiles/list_profiles_owners.html', context)


def list_profiles_walkers(request):
    dog_sitters = Profile.objects.filter(category='Dog sitter')

    context = {
        'DogSitter': dog_sitters,
    }

    return render(request, 'profiles/list_profiles_sitters.html', context)


@login_required
def profile_details(request, pk):
    profile = Profile.objects.get(pk=pk)

    context = {
        'profile': profile,
    }
    return render(request, 'profiles/list_profile_details.html', context)
