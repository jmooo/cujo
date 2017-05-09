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
