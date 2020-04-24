from django import template
from ..models import CoffeeBeans, PlaceCategory

register = template.Library()


@register.inclusion_tag('include/place_category_links.html')
def place_category_links():
    return {
        'place_list': PlaceCategory.objects.all()
    }


@register.filter(name='sum_price')
def sum_price(value, args):
    return value * args
