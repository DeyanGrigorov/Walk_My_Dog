from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

from walk_my_dog.profile_auth.models import Profile


def list_profiles_owners(request):
    dog_owners = Profile.objects.filter(category='Dog owner')
    dog_owners_paginator = Paginator(dog_owners, 3)
    page_num = request.GET.get('page')
    page = dog_owners_paginator.get_page(page_num)

    context = {
        'page': page,
    }

    return render(request, 'profiles/list_profiles_owners.html', context)


def list_profiles_sitters(request):
    dog_sitters = Profile.objects.filter(category='Dog sitter')
    dog_sitters_paginator = Paginator(dog_sitters, 3)
    page_num = request.GET.get('page')
    page = dog_sitters_paginator.get_page(page_num)


    context = {
        'page': page,
    }

    return render(request, 'profiles/list_profiles_sitters.html', context)


@login_required
def profile_details(request, pk):
    profile = Profile.objects.get(pk=pk)

    context = {
        'profile': profile,
    }
    return render(request, 'profiles/list_profile_details.html', context)
