import uuid
from datetime import datetime, timedelta
from django.utils import timezone
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager
from django.utils.translation import gettext_lazy as _


def user_directory_path(instance, filename):
    return f'profile-photo/{instance.id}/{filename}'



class User(AbstractBaseUser, PermissionsMixin):
    id               = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email            = models.EmailField(_('email address'), unique=True, blank=False)
    username         = models.CharField(_('user name'), max_length=150, unique=True)
    password         = models.CharField(_('password'), blank=False)
    first_name       = models.CharField(_('first name'), max_length=250, blank=True, null=True)
    last_name        = models.CharField(_('last name'), max_length=250, blank=True, null=True)
    mobile           = models.IntegerField(_('mobile number'), blank=True, null=True)
    about            = models.TextField(_('about'), max_length=500, blank=True, null=True)

    # date_joined     = models.DateTimeField(auto_now_add=True)
    date_joined     = models.DateTimeField(default=timezone.now)
    updated_at      = models.DateTimeField(auto_now=True)
    last_login      = models.DateTimeField(auto_now=True)

    is_staff        = models.BooleanField(default= False)
    is_superuser    = models.BooleanField(default= False)
    is_active       = models.BooleanField(default= False)

    profile_photo   = models.ImageField(_('profile photo'), upload_to=user_directory_path, blank=True)

    # unverified_email = models.EmailField(blank=True)
    # old_email_update_code = models.CharField(max_length=256, blank=True)
    # new_email_verification_code = models.CharField(max_length=256, blank=True)


    class Meta:
        # verbose_name_plural = 'Users'
        db_table = 'Users'
        ordering = ['-date_joined']

    objects = UserManager()

    USERNAME_FIELD  = 'email'     
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        full_name = ' '.join([self.first_name, self.last_name])
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username