from django.db import models
from datetime import timedelta

from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff,
                is_superuser, **extra_fields):

        email = self.normalize_email(email)
        user = self.model(username = username, email=email, is_active=True,
                is_staff = is_staff, is_superuser = is_superuser, **extra_fields)
        user.set_password(password)
        user.save( using = self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False,
                False, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True,
                True, **extra_fields)



"""
This is a example of Custom User Model in Django

PermissionsMixin is if you need the Permissions Module of django

"""
class User(AbstractBaseUser, PermissionsMixin):

    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    # This field "id" is not requerid, but i put this for example and more clearly
    id          = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    username    = models.CharField(max_length=100, unique=True)
    email       = models.EmailField(unique=True)
    first_name  = models.CharField(max_length=100)
    last_name   = models.CharField(max_length=100)
    gender      = models.CharField(choices=gender_choices, max_length=50)
    avatar      = models.URLField()  # Url compatible with social login
    created_on  = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name','email','gender']


    # This function return a String of the Object, similar toString on Java.
    def __str__(self):
        return "%s %s"%(self.first_name, self.last_name)


    # This function or method return the short name of the user
    def get_short_name(self):
        return self.first_name


    # This function return the Full Name of the User
    def full_name(self):
        return title('%s %s' % (self.first_name, self.last_name))


    # This meta Class is to put a diferent name of the table in to the database.
    class Meta:

        db_table = 'users'
