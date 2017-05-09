from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.postgres.search import SearchQuery, SearchRank
from django.db.models import F

from .models import Ticket
from .forms import TicketForm


def ticket_list(request):
    tickets = Ticket.objects.all().order_by('-date_modified')
    return render(request, 'ticket/ticket_list.html', {'tickets': tickets})


def ticket_new(request):
    ticket = Ticket()
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user.get_full_name()
            ticket.modified_by = request.user.get_full_name()
            ticket.date_created = timezone.now()
            ticket.date_modified = timezone.now()
            ticket.save()
            return redirect('ticket_edit', pk=ticket.pk)
    else:
        form = TicketForm(instance=ticket)

    return render(request, 'ticket/ticket_edit.html', {'form': form})


def ticket_edit(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.date_modified = timezone.now()
            ticket.modified_by = request.user.get_full_name()
            ticket.save()
            return redirect('ticket_edit', pk=ticket.pk)
    else:
        form = TicketForm(instance=ticket)

    return render(request, 'ticket/ticket_edit.html', {'form':form, 'ticket':ticket})


def ticket_search(request):
    q = request.GET.get('q')
    if q:
        query = SearchQuery(q)
        result = Ticket.objects.annotate(rank=SearchRank(F('search_vector'), query)) \
                    .filter(search_vector=query) \
                    .order_by('-rank')

        return render(request, 'ticket/ticket_list.html',
                        {'tickets':result, 'ticket_list_name':'Search Results'})

    return redirect('ticket_list', '')
