from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from walk_my_dog.walkmydog_auth.models import WalkMyDogUser


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "password"
        self.fields['password2'].label = "confirm password"

    email = forms.CharField(
        widget=forms.EmailInput
            (
            attrs={'class': "form-row"}
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput
            (
            attrs={
                'class': "form-row",
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput
            (
            attrs={'class': "form-row"}
        )
    )

    city = forms.CharField(
        widget=forms.TextInput
            (
            attrs={'class': "form-row"}
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput
            (
            attrs={'class': "form-row"}
        ))

    password2 = forms.CharField(
        widget=forms.PasswordInput
            (

            attrs={'class': "form-row"}
        )
    )

    class Meta:
        model = WalkMyDogUser
        fields = ("email", "first_name", "last_name", "city", "category", "password1", "password2")

    def clean(self):
        super(SignUpForm, self).clean()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if len(first_name) < 2:
            self._errors['first_name'] = self.error_class(['Minimum 2 characters required for first name'])
        if len(last_name) < 4:
            self._errors['last_name'] = self.error_class(['Minimum 4 characters required for last name'])

        return self.cleaned_data


class LoginForm(forms.Form):
    user = None
    email = forms.EmailField(
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('password'),
        )

        if not self.user:
            raise ValidationError('Email and/or password incorrect')

    def save(self):
        return self.user


class UserForm(forms.ModelForm):
    class Meta:
        model = WalkMyDogUser
        fields = ('first_name', 'last_name', 'city')
