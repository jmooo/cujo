from django import template
from django.contrib.humanize.templatetags.humanize import naturaltime, naturalday
from django.utils import timezone

register = template.Library()


@register.filter
def humanizetime(time):
    """ Blend Humanize naturaltime and naturalday for a cleaner display
    """
    timeDiff = timezone.now() - time
    if timeDiff.days > 0:
        return naturalday(time)
    return naturaltime(time)

@register.filter
def user_exists(user):
    """ If an AccountUser has been deleted, created_by/modified_by fields will be set NULL
        so display that gracefully
    """
    if user:
        return user
    return 'Unknown'
