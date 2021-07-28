from django.db import transaction
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from walk_my_dog.walkmydog_auth.forms import LoginForm, SignUpForm

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

