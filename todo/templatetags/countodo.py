from django import template
from todo.models import Todo

register = template.Library()

@register.simple_tag
def count_posts_of(user):
	return Todo.objects.filter(user =user).count()