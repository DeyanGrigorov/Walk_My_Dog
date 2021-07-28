from django import forms

from walk_my_dog.profile_auth.models import Profile


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    category = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'city', 'profile_image', 'category')
