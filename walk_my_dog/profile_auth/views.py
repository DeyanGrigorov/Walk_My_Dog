from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from walk_my_dog.profile_auth.forms import ProfileForm
from walk_my_dog.profile_auth.models import Profile
from walk_my_dog.walkmydog_auth.forms import UserForm


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('update profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user)
    return render(request, 'accounts/user_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


# @login_required
# def profile_details(request):
#     profile = Profile.objects.get(pk=request.user.id)
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile, )
#         if form.is_valid():
#             form.save()
#             return redirect('profile details')
#     else:
#         form = ProfileForm(instance=profile)
#
#     context = {
#         'form': form,
#         'profile': profile,
#     }
#
#     return render(request, 'accounts/user_profile.html', context)

