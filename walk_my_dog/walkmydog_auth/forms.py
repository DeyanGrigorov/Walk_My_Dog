from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    User_type = [
        ('Dog owner', 'Dog owner'),
        ('Dog walker', 'Dog walker')

    ]

    user_type = (
        forms.MultipleChoiceField(
            choices=User_type,
            widget=forms.CheckboxSelectMultiple(),
        )
    )

    def clean_user_type(self):
        if len(self.cleaned_data['user_type']) > 1:
            raise forms.ValidationError('Select no more than 1.')
        return self.cleaned_data['user_type']

    first_name = forms.CharField(
        max_length=30,
    )

    last_name = forms.CharField(
        max_length=30,
    )

    email = forms.EmailField()

    city = forms.CharField(
        max_length=50,
    )

    class Meta:
        model = UserModel
        fields = ("first_name", "last_name", "email", "city", 'user_type' ,"password1", "password2")


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
