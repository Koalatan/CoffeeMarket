from django import template
from ..models import CoffeeBeans, PlaceCategory


register = template.Library()


@register.inclusion_tag('include/place_category_links.html')
def place_category_links():
    return {
        'place_list': PlaceCategory.objects.all()
    }