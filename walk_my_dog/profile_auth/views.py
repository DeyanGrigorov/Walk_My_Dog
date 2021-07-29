from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from walk_my_dog.profile_auth.forms import ProfileForm
from walk_my_dog.walkmydog_auth.forms import UserForm
from walk_my_dog.walkmydog_auth.models import WalkMyDogUser


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('update profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/user_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })



# def delete_profile(request):
#     profile = Profile.objects.all()
#     user = WalkMyDogUser.objects.get(email='email')
#     profile.delete()
#     user.delete()
#     return redirect("landing page")
# # deletes everything!
@login_required
def delete_profile(request):
    WalkMyDogUser.objects.get(id=request.user.id).delete()
    return redirect('landing page')
