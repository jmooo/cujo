from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class AccountUserManager(BaseUserManager):

    def create_user(self, email, password, first_name, last_name, account, **extra_fields):
        if not email:
            raise ValueError('Please enter an email address')
        if not first_name:
            raise ValueError('Please enter a first name')
        if not last_name:
            raise ValueError('Please enter a last name')
        if not account:
            raise ValueError('Please enter an account id')

        email = self.normalize_email(email)
        user = self.model(email=email,
                            first_name=first_name,
                            last_name=last_name,
                            account=account,
                            **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, first_name, last_name, account, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        # From the cli you're going to have to enter an int, resolve that to an Account object
        account = Account.objects.get(pk=account)

        return self.create_user(email,
                                password=password,
                                first_name=first_name,
                                last_name=last_name,
                                account=account,
                                **extra_fields)


class AccountUser(AbstractBaseUser, PermissionsMixin):
    """ Extend Django User model to remove username and make email the only login method
    """
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    first_name = models.CharField(_('first name'), max_length=50, blank=False)
    last_name = models.CharField(_('last name'), max_length=50, blank=False)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)

    is_staff = models.BooleanField(_('staff user'), default=False,
        help_text=_('Allow the user to log into the admin site'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Is the user active? Uncheck this instead of deleting users'))
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)

    objects = AccountUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'account',]

    def get_full_name(self):
        full_name = '{0} {1}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    class Meta:
        """ Change the display name from 'Account users' in the admin panel
        """
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Account(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
