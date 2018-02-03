from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login')),
    path('login/', auth_views.login, {'template_name': 'account/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/login'}, name='logout'),
    path('password_reset/', auth_views.password_reset,
         {'template_name': 'account/password_reset_form.html',
          'email_template_name': 'account/password_reset_email.html',
          'subject_template_name': 'account/password_reset_subject.txt'}, name='password_reset'),
    path('password_reset/done/', auth_views.password_reset_done,
         {'template_name': 'account/password_reset_done.html'}, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.password_reset_confirm,
         {'template_name': 'account/password_reset_confirm.html'}, name='password_reset_confirm'),
    path('reset/done/', auth_views.password_reset_complete,
         {'template_name': 'account/password_reset_complete.html'}, name='password_reset_complete'),
]
