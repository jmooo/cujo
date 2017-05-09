from django.db import models
from django.utils import timezone
from django.contrib.postgres.search import SearchVector, SearchVectorField
from django.contrib.postgres.indexes import GinIndex


class TicketManager(models.Manager):
    """ Add documents to the queryset
    """
    def with_documents(self):
        vector = SearchVector('customer', weight='A') + \
                    SearchVector('address', weight='B') + \
                    SearchVector('work_requested', weight='D') + \
                    SearchVector('work_completed', weight='D')
        return self.get_queryset().annotate(document=vector)


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
    search_vector = SearchVectorField(null=True)

    objects = TicketManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if 'update_fields' not in kwargs or 'search_vector' not in kwargs['update_fields']:
            instance = self._meta.default_manager.with_documents().get(pk=self.pk)
            instance.search_vector = instance.document
            instance.save(update_fields=['search_vector'])

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector'])
        ]

    def __str__(self):
        return self.customer
