from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "first_name"]


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["image", "about", "githubusername"]
        labels = {
            "image": "Profile Pic (500x500 is preferred resolution)",
            "about": "About you (max 200 words)",
            "githubusername":
            "Github Username ( if you wanna let others see it )",
        }
        widgets = {"image": forms.FileInput()}
