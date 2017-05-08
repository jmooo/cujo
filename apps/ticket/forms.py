from django import forms

from .models import Ticket


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('client', 'salesperson', 'description', 'created_date',
                'address', 'address_apt', 'address_city', 'address_state',
                'address_zip')
