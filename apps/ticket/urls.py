from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='ticket_list')),
    url(r'^ticket/$', views.TicketListView.as_view(), name='ticket_list'),
    url(r'^ticket/new/$', views.ticket_new, name='ticket_new'),
    url(r'^ticket/edit/(?P<pk>\d+)/$', views.ticket_edit, name='ticket_edit'),
]
