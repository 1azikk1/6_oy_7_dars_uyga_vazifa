from django import template
from ..models import Species, Flowers

register = template.Library()


@register.simple_tag
def all_species():
    return Species.objects.all()

