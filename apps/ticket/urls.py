from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='ticket-list')),
    url(r'^ticket/$', views.TicketListView.as_view(), name='ticket-list'),
    url(r'^ticket/new/$', views.TicketCreateView.as_view(), name='ticket-new'),
    url(r'^ticket/(?P<pk>[0-9]+)/$', views.TicketUpdateView.as_view(), name='ticket-edit'),
    url(r'^ticket/(?P<pk>[0-9]+)/delete/$', views.TicketDeleteView.as_view(), name='ticket-delete'),
]
