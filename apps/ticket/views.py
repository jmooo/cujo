from django.shortcuts import render, get_object_or_404
from .models import Ticket
from .forms import TicketForm


def ticket_list(request):
    tickets = Ticket.objects.all().order_by('created_date')
    return render(request, 'ticket/ticket_list.html', {'tickets': tickets})

def ticket_edit(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'ticket/ticket_edit.html', {'ticket': ticket})
