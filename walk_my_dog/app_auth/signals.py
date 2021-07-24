from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    user = None
    email = forms.EmailField(

    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Email and/or password incorrect')

    def save(self):
        return self.user
