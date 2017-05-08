from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.request_list, name='request_list'),
    url(r'^editrequest/(?P<pk>\d+)/$', views.edit_request, name='edit_request'),
]
