from django.contrib.postgres.search import SearchQuery, SearchRank
from django.db.models import F
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Ticket
from .forms import TicketForm

class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket

    def get_queryset(self):
        qs = super().get_queryset().order_by('-date_modified')

        q = self.request.GET.get('q')
        if q:
            query = SearchQuery(q)
            qs = qs.annotate(rank=SearchRank(F('search_vector'), query)) \
                    .filter(search_vector=query) \
                    .order_by('-rank')
        return qs

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            q=self.request.GET.get('q', "")
        )


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.modified_by = form.instance.created_by
        return super(TicketCreateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('ticket-edit', args = (self.object.id,))


class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Ticket
    form_class = TicketForm

    def form_valid(self, form):
        form.instance.modified_by = self.request.user
        return super(TicketUpdateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('ticket-edit', args = (self.object.id,))


class TicketDeleteView(LoginRequiredMixin, DeleteView):
    model = Ticket
    form_class = TicketForm
    success_url = reverse_lazy('ticket-list')
