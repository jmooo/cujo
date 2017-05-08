from django.db import models
from django.utils import timezone
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField, USZipCodeField

class Ticket(models.Model):
    creator = models.ForeignKey('auth.User')
    salesperson = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    address_apt = models.CharField(max_length=255, blank=True)
    address_city = models.CharField(max_length=100)
    address_state = USStateField(choices=STATE_CHOICES)
    address_zip = USZipCodeField(max_length=12)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.client
