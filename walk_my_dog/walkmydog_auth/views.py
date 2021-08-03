from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

from walk_my_dog.walkmydog_auth.forms import LoginForm, SignUpForm


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
            return redirect('update profile')
    else:
        form = SignUpForm
    context = {
        'form': form
    }

    return render(request, 'accounts/sign_up.html', context)


def sign_out_user(request):
    logout(request)
    return redirect('landing page')
