import pytest
from django.contrib.auth import get_user_model

from apps.account.models import Account


@pytest.fixture
@pytest.mark.django_db
def account(request):
    return Account.objects.create(name="Test Account")


@pytest.fixture
@pytest.mark.django_db
def accountuser(request, account):
    required_fields = {
        'email': 'test@example.com',
        'first_name': 'Test',
        'last_name': 'User',
        'password': 'Test Pa$$word',
    }
    return get_user_model().objects.create_user(account=account, **required_fields)
