from django import template
from resources.models import Progress

register = template.Library()


@register.simple_tag
def notdone(user, resource):
    if Progress.objects.filter(user=user, resource=resource, isdone=True):
        return True
    else:
        return False
