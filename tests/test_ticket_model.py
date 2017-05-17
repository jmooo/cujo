import pytest

from apps.ticket.models import Ticket


@pytest.mark.django_db
class TestTicketModel:

    required_fields = {
        'customer': 'Test Customer',
        'salesperson': 'Test Salesperson',
        'address': 'Test Address',
    }
    
    def test_create_ticket(self, account):
        ticket = Ticket.objects.create(account=account, **self.required_fields)
        assert str(ticket) == self.required_fields['customer']
