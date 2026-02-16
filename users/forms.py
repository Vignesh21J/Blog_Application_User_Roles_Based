from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                raise ValidationError(
                    "Invalid username or password.",
                    code='invalid_login'
                )

            if not user.check_password(password):
                raise ValidationError(
                    "Invalid username or password.",
                    code='invalid_login'
                )

            if not user.is_active:
                raise ValidationError(
                    "Your account is awaiting admin approval. Please contact the administrator.",
                    code='inactive'
                )

            self.user_cache = user

        return self.cleaned_data