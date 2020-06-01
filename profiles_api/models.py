from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ manager for user profiles """

    def create_user(self, email, name, password= None):
        """ Create a new user profile """
        if not email:
            raise ValueError('User must have email address')

        email = self.normalize_email(email)
        user = self.model(email= email, name= name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email=None, name=None, password=None):
        """ Create a new superuser """
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in system """
    email = models.EmailField(max_length= 255, unique= True)
    name =  models.CharField(max_length= 255)
    is_active = models.BooleanField(default= True)
    is_staff =  models.BooleanField(default= False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrieve full name of user """
        return self.name

    def get_short_name(self):
        """ Retrieve short name of user """
        return self.name


    def __str__(self):
        """ Retrieve string representatin of user """
        return self.email
