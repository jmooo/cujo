from django.test import TestCase
from django.contrib.auth import get_user_model
import pytest

from apps.account.models import Account

@pytest.mark.django_db(transaction=True)
class AccountModelTest(TestCase):

    user_email = "test@example.com"
    user_password = "Test Pa$$word"
    user_first_name = "Test"
    user_last_name = "User"
    account_name = "Test Account"

    def setUp(self):
        self.account = Account.objects.create(name=self.account_name)

        # DRY, make it easier to blank out an individual key to test ValueErrors
        self.expected_fields = {
            'email': self.user_email,
            'first_name': self.user_first_name,
            'last_name': self.user_last_name,
            'password': self.user_password,
            'account': self.account,
        }

    def tearDown(self):
        self.account.delete()

    def test_account_creation(self):
        self.assertEqual(self.account.__str__(), self.account_name)

    def test_create_user(self):
        user = get_user_model().objects.create_user(**self.expected_fields)
        self.assertEqual(user.email, self.user_email)
        self.assertEqual(user.first_name, self.user_first_name)
        self.assertEqual(user.last_name, self.user_last_name)
        self.assertEqual(user.account, self.account)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.get_short_name(), self.user_first_name)
        self.assertEqual(user.get_full_name(), '{0} {1}'.format(self.user_first_name, self.user_last_name))

    def test_create_superuser(self):
        self.expected_fields['account'] = self.account.pk
        user = get_user_model().objects.create_superuser(**self.expected_fields)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_empty_email(self):
        self.expected_fields['email'] = ''
        self.assertRaises(ValueError, get_user_model().objects.create_user, **self.expected_fields)

    def test_empty_first_name(self):
        self.expected_fields['first_name'] = ''
        self.assertRaises(ValueError, get_user_model().objects.create_user, **self.expected_fields)

    def test_empty_last_name(self):
        self.expected_fields['last_name'] = ''
        self.assertRaises(ValueError, get_user_model().objects.create_user, **self.expected_fields)

    def test_empty_account(self):
        self.expected_fields['account'] = ''
        self.assertRaises(ValueError, get_user_model().objects.create_user, **self.expected_fields)
