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

        # Only return tickets attached to the user's account!
        return qs.filter(account_id=self.request.user.account_id)

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            q=self.request.GET.get('q', "")
        )


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm

    def form_valid(self, form):
        """ Set internal fields the user can't edit """
        form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        form.instance.account_id = self.request.user.account_id
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('ticket-edit', args = (self.object.id,))


class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Ticket
    form_class = TicketForm

    def get_queryset(self):
        """ Only return ticket if it is attached to user's account """
        return super().get_queryset().filter(account_id=self.request.user.account_id)

    def form_valid(self, form):
        """ Set internal fields the user can't edit """
        form.instance.modified_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('ticket-edit', args = (self.object.id,))


class TicketDeleteView(LoginRequiredMixin, DeleteView):
    model = Ticket
    form_class = TicketForm
    success_url = reverse_lazy('ticket-list')

    def get_queryset(self):
        """ Only return ticket if it is attached to users account """
        return super().get_queryset().filter(account_id=self.request.user.account_id)
