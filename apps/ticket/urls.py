from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ticket_list, name='ticket_list'),
    url(r'^ticket/edit/(?P<pk>\d+)/$', views.ticket_edit, name='ticket_edit'),
]
