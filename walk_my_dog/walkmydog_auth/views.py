from django.db import transaction
from importlib._common import _
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from walk_my_dog.walkmydog_auth.forms import LoginForm, SignUpForm, ProfileForm, UserForm
from walk_my_dog.walkmydog_auth.models import Profile
from django.contrib import messages

def sign_in_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing page')
    else:
        form = LoginForm
    context = {
        'form': form,
    }

    return render(request, 'accounts/sign_in.html', context)


def sign_up_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Sign up successful.')
            return redirect('landing page')
        messages.error(request, 'Unsuccessful sign up. Invalid information.')
    else:
        form = SignUpForm()
    context = {
        'form': form
    }

    return render(request, 'accounts/sign_up.html', context)


def sign_out_user(request):
    logout(request)
    return redirect('landing page')


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile, )
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'accounts/user_profile.html', context)


# class UserEditView(generic.UpdateView):
#     form_class = ProfileForm
#     template_name = 'accounts/user_profile.html'
#     success_url = reverse_lazy('profile details')
#
#     def get_object(self, **kwargs):
#         return self.request.user

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('profile details')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user)
    return render(request, 'accounts/user_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
