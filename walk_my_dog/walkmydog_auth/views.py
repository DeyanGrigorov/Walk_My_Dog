from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

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


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/sign_up.html'
    success_url = reverse_lazy('update profile')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result


def sign_out_user(request):
    logout(request)
    return redirect('landing page')
