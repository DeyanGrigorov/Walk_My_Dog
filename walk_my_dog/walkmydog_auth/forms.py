from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from walk_my_dog.walkmydog_auth.models import WalkMyDogUser

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
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

# class ProfileForm(forms.ModelForm):
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
#     category = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
#     class Meta:
#         model = Profile
#         fields = ('first_name', 'last_name', 'city', 'profile_image', 'category')
