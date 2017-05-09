from django.db import models
from django.utils import timezone


class Ticket(models.Model):
    created_by = models.CharField(max_length=255)
    modified_by = models.CharField(max_length=255)
    salesperson = models.CharField(max_length=255)
    customer = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)
    date_completed = models.DateField(null=True, blank=True)
    work_requested = models.TextField()
    work_completed = models.TextField(null=True, blank=True)
    installers = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.client
