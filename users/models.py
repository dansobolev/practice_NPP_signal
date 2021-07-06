from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .enums import UserTypeEnum


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, null=True)
    # birth_date = models.DateField(verbose_name='Date of birth', null=True, blank=True)
    user_type = models.IntegerField(choices=UserTypeEnum.choices(), null=True, blank=True)

    def __str__(self):
        return f'{self.user}, {self.firstname} {self.lastname}'


"""@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()"""
