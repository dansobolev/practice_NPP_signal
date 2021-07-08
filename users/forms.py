from django.contrib.auth import get_user_model
from django import forms
from django.http import JsonResponse

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
    birth_date = forms.DateField()
    phone_number = forms.CharField()
    department = forms.CharField()
    personnel_number = forms.IntegerField()
    user_type = forms.CharField()

    def validate_user(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.filter(username__iexact=username).get()
        except User.DoesNotExist:
            return False
        except User.MultipleObjectsReturned:
            return JsonResponse({'message': 'Пользователь с таким никнеймом уже существует.'})

    def check_user_email(self):
        email = self.cleaned_data.get('email')
        try:
            UserProfile.objects.filter(email__iexact=email).get()
        except UserProfile.DoesNotExist:
            return False
        except UserProfile.MultipleObjectsReturned:
            return JsonResponse({'message': 'Пользователь с таким email уже существует.'})

    def check_user_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        try:
            UserProfile.objects.filter(phone_number__iexact=phone_number).get()
        except UserProfile.DoesNotExist:
            return False
        except UserProfile.MultipleObjectsReturned:
            return JsonResponse({'message': 'Пользователь с таким номером телефона уже существует.'})


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
