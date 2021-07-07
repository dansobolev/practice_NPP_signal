from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

from .exceptions import UserAlreadyExistsException, UserNotFoundException
from .models import UserProfile
from .forms import RegisterForm, LoginForm
from .enums import UserTypeEnum


can_edit_perm = [i.value for i in UserTypeEnum if i.value <= 2]


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if not form.check_user_email():
                user_profile = UserProfile.objects.filter(email__iexact=email)
                if user_profile is not None:
                    UserAlreadyExistsException('User with this username is already exists. Try another one.')

                user_object = User.objects.create_user(username=username, password=form.cleaned_data.get('password'))
                user_object.save()
                new_profile_user = UserProfile.objects.create(
                    user=user_object,
                    email=form.cleaned_data.get('email'),
                    firstname=form.cleaned_data.get('firstname'),
                    lastname=form.cleaned_data.get('lastname'),
                    middlename=form.cleaned_data.get('middlename'),
                    # birth_date=form.cleaned_data.get('birth_date'),
                    user_type=form.cleaned_data.get('user_type'),
                )
                new_profile_user.save()

                if new_profile_user.user_type in can_edit_perm:
                    new_profile_user.user_permission.set(
                        ['signal_app.change_assembly', 'signal_app.view_assembly',
                         'signal_app.change_baseproduct', 'signal_app.view_baseproduct'])
                else:
                    new_profile_user.user_permission.set(
                        ['signal_app.view_assembly', 'signal_app.view_baseproduct'])

                created_user = UserProfile.objects.filter(email__iexact=email)
                print(created_user)
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            print(User.objects.filter(username=username))
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                print(user)
                login(request, user)
                print("Successful")
            else:
                raise UserNotFoundException("User not found")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
