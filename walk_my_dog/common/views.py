from django.shortcuts import render

from walk_my_dog.profile_auth.models import Profile


def landing_page(request):

    return render(request, 'base/Index.html')
