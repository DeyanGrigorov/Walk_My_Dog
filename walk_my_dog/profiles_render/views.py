from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from walk_my_dog.profile_auth.models import Profile
from walk_my_dog.profiles_render.models import Like


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
    profile.likes_count = profile.like_set.count
    like_object_by_user = profile.like_set.filter(user_id=request.user.id).first()

    context = {
        'profile': profile,
        'is_liked': like_object_by_user is  None,
    }
    return render(request, 'profiles/list_profile_details.html', context)


def like_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    like_object_by_user = profile.like_set.filter(user_id=request.user.id).first()
    if like_object_by_user:
        like_object_by_user.delete()
    else:

        like = Like(
            profile=profile,
            user=request.user,
        )
        like.save()
    return redirect('list profile details', pk)
