from django import template
from notes.models import Notes

register = template.Library()


@register.simple_tag
def count_posts_of(user):
    return Notes.objects.filter(user=user).count()
