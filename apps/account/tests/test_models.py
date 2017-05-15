from django.test import TestCase

from ..models import Account, AccountUser

class AccountModelTest(TestCase):

    def setUp(self):
        self.account = Account.objects.create(name="Test Account")
        self.accountuser = AccountUser.objects.create_user(first_name="Test",
                                            last_name="AccountUser",
                                            account=self.account,
                                            email="test@accountuser.com",
                                            password="test password",)

    def tearDown(self):
        self.account.delete()
        self.accountuser.delete()

    def test_account_creation(self):
        self.assertTrue(isinstance(self.account, Account))
        self.assertEqual(self.account.__str__(), self.account.name)

    def test_accountuser_creation(self):
        self.assertTrue(isinstance(self.accountuser, AccountUser))
        self.assertEqual(self.accountuser.get_short_name(), self.accountuser.first_name)
        self.assertEqual(self.accountuser.get_full_name(),
                        '{0} {1}'.format(self.accountuser.first_name, self.accountuser.last_name))
