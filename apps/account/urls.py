from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='login')),
    url(r'^login/$', auth_views.login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
]
