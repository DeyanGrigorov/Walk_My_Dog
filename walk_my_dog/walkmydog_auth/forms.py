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
    email = forms.CharField(
        widget=forms.EmailInput
            (
            attrs={'class': "form-row"}
        )
    )
    #
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
        fields = ("first_name", "last_name", "email", "city", "category", "password1", "password2")


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


class UserForm(forms.ModelForm):
    class Meta:
        model = WalkMyDogUser
        fields = ('first_name', 'last_name', 'city')
