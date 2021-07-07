import json

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

from .exceptions import UserAlreadyExistsException, UserNotFoundException
from .models import UserProfile
from .forms import RegisterForm, LoginForm
from .enums import UserTypeEnum


can_edit_perm = [i.value for i in UserTypeEnum if i.value <= 2]


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(json.loads(request.body))
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if not form.check_user_email() \
                    and not form.check_user_phone_number() and not form.validate_user():
                user_object = User.objects.create_user(username=username, password=form.cleaned_data.get('password'))
                user_object.save()
                new_profile_user = UserProfile.objects.create(
                    user=user_object,
                    email=form.cleaned_data.get('email'),
                    firstname=form.cleaned_data.get('firstname'),
                    lastname=form.cleaned_data.get('lastname'),
                    middlename=form.cleaned_data.get('middlename'),
                    birth_date=form.cleaned_data.get('birth_date'),
                    phone_number=form.cleaned_data.get('phone_number'),
                    department=form.cleaned_data.get('department'),
                    personnel_number=form.cleaned_data.get('personnel_number'),
                    user_type=form.cleaned_data.get('user_type'),
                )

                new_profile_user.save()
    else:
        form = RegisterForm()

    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"logged_in_user": user})
            else:
                return JsonResponse({'message': 'Неверный логин или пароль.'})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
