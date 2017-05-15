from django.test import TestCase

from ..models import Ticket
from apps.account.models import Account

class TicketTest(TestCase):

    def setUp(self):
        self.account = Account.objects.create(name="Test Account")
        self.ticket = Ticket.objects.create(account=self.account,
                                            customer="Test Customer",
                                            salesperson="Test Salesperson",
                                            phone="(111) 222-3333",
                                            email="test@accountuser.com",)

    def tearDown(self):
        # This should CASCADE delete the ticket as well
        self.account.delete()

    def test_ticket_creation(self):
        self.assertTrue(isinstance(self.ticket, Ticket))
        self.assertEqual(self.ticket.__str__(), self.ticket.customer)
        self.assertEqual(self.account, self.ticket.account)
