from django.db import models
from django.contrib.auth.models import User

from .enums import UserTypeEnum


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, null=True)
    birth_date = models.DateField(verbose_name='Date of birth', null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100, help_text='Отдел служащего')
    personnel_number = models.IntegerField(help_text='Табельный номер')
    user_type = models.IntegerField(choices=UserTypeEnum.choices(), null=True, blank=True)

    def __str__(self):
        return f'{self.user}, {self.firstname} {self.lastname}'
