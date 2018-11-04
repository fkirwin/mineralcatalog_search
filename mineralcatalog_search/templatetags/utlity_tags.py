import random

from django import template

from minerals.models import Mineral

register = template.Library()


@register.simple_tag
def random_mineral():
    record = random.randint(1, Mineral.objects.count()+1)
    link = Mineral.objects.get(pk=record)
    return link.id

@register.filter('concatenate')
def concatenate(arg1, arg2):
    """concatenate"""
    return str(arg1) + str(arg2)