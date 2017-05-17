from django.contrib.auth import get_user_model
import pytest


@pytest.mark.django_db
class TestAccountModel:

    required_fields = {
        'email': 'test@example.com',
        'first_name': 'Test',
        'last_name': 'User',
        'password': 'Test Pa$$word',
    }

    def test_account_creation(self, account):
        assert str(account) == account.name

    def test_create_user(self, account):
        user = get_user_model().objects.create_user(account=account, **self.required_fields)
        assert user.email == self.required_fields['email']
        assert user.first_name == self.required_fields['first_name']
        assert user.last_name == self.required_fields['last_name']
        assert user.account == account
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser
        assert user.get_short_name() == self.required_fields['first_name']
        assert user.get_full_name() == '{0} {1}'.format(
            self.required_fields['first_name'], self.required_fields['last_name'])

    def test_create_superuser(self, account):
        user = get_user_model().objects.create_superuser(account=account.pk, **self.required_fields)
        assert user.is_active
        assert user.is_staff
        assert user.is_superuser

    def test_empty_email(self, account):
        fields = self.required_fields.copy()
        fields['email'] = ''
        with pytest.raises(ValueError) as excinfo:
            get_user_model().objects.create_user(account=account, **fields)

    def test_empty_first_name(self, account):
        fields = self.required_fields.copy()
        fields['first_name'] = ''
        with pytest.raises(ValueError) as excinfo:
            get_user_model().objects.create_user(account=account, **fields)

    def test_empty_last_name(self, account):
        fields = self.required_fields.copy()
        fields['last_name'] = ''
        with pytest.raises(ValueError) as excinfo:
            get_user_model().objects.create_user(account=account, **fields)

    def test_empty_account(self, account):
        fields = self.required_fields.copy()
        fields['account'] = ''
        with pytest.raises(ValueError) as excinfo:
            get_user_model().objects.create_user(**fields)
