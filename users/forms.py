from django.contrib.auth import get_user_model
from django import forms

from .exceptions import UserAlreadyExistsException, UserWithThisEmailAlreadyExistsException
from .models import UserProfile

User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    middlename = forms.CharField()
    user_type = forms.IntegerField()

    def validate_user(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username__iexact=username)
        if user is not None:
            raise UserAlreadyExistsException('User with this username is already exists. Try another one.')

    def check_user_email(self):
        email = self.cleaned_data.get('email')
        try:
            UserProfile.objects.filter(email__iexact=email).get()
        except UserProfile.DoesNotExist:
            print("User not found")
        except UserProfile.MultipleObjectsReturned:
            raise UserWithThisEmailAlreadyExistsException('User with this email is already exists')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
