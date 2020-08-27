from django import template
from creator.models import Product

register = template.Library()

@register.simple_tag
def count_products_of(user):
    return Product.objects.filter(user =user).count()
