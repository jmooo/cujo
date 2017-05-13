from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import AccountUser

class AccountUserCreationForm(UserCreationForm):

    class Meta:
        model = AccountUser
        fields = []

class AccountUserChangeForm(UserChangeForm):

    class Meta:
        model = AccountUser
        fields = []
