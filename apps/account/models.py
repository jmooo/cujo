from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class AccountUserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, **extra_fields):
        if not email:
            raise ValueError('Please enter an email address')
        if not first_name:
            raise ValueError('Please enter a first name')
        if not last_name:
            raise ValueError('Please enter a last name')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password=password, first_name=first_name,
                                last_name=last_name, **extra_fields)


class AccountUser(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    username = models.CharField(unique=False, max_length=150)
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = AccountUserManager()


class Account(models.Model):
    pass
