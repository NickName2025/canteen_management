from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User

        fields = (
            "fio",
            "school_class",
            "username",
            "password1",
            "password2"
        )

    fio = forms.CharField()
    school_class = forms.CharField()
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()