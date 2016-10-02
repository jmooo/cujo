from django.utils import timezone


def timezone_default():
    """ This method is used when setting the initial value
        for datetime fields. This makes it easier to mock """
        
    return timezone.now()
