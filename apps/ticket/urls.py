from django.urls import path
from . import views

urlpatterns = [
    path('ticket/', views.TicketListView.as_view(), name='ticket-list'),
    path('ticket/new/', views.TicketCreateView.as_view(), name='ticket-new'),
    path('ticket/<int:pk>/', views.TicketUpdateView.as_view(), name='ticket-edit'),
    path('ticket/<int:pk>/delete/', views.TicketDeleteView.as_view(), name='ticket-delete'),
]
