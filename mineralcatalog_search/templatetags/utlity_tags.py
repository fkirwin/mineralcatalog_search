import random

from django import template
from django.urls import reverse

from minerals.models import Mineral
from minerals import views as mineral_views

register = template.Library()


@register.simple_tag
def random_mineral():
    """
    Template tag for a random mineral to be generated for the layout.
    Use this as a link in the anchor tag.
    """
    record = random.randint(Mineral.objects.all().order_by("id")[0].id,
                            Mineral.objects.all().order_by("-id")[0].id)
    link = Mineral.objects.get(pk=record)
    return reverse('minerals:detail', kwargs={"pk":link.id})

@register.simple_tag
def menu_dict():
    """
    Gets just the names, first letter and links for each mineral.
    """
    mineral_names_ids = {}
    for mineral in Mineral.objects.all().values('id', 'name', 'group'):
        if mineral['group'] in mineral_names_ids.keys():
            mineral_names_ids[mineral['group']].append(
                                             (mineral['name'],
                                              reverse('minerals:detail', kwargs={"pk": mineral['id']}))
                                             )
        else:
            mineral_names_ids[mineral['group']] = [
                                         (mineral['name'],
                                         reverse('minerals:detail', kwargs={"pk": mineral['id']}))
                                        ]
    return mineral_names_ids

@register.simple_tag
def alpha_dict():
    """
    Gets just the names, first letter and links for each mineral.
    """
    mineral_names_ids = {}
    for mineral in Mineral.objects.all().values('id', 'name'):
        letter = mineral['name'][0].upper()
        if letter in mineral_names_ids.keys():
            mineral_names_ids[letter].append(
                                             (mineral['name'],
                                              reverse('minerals:detail', kwargs={"pk": mineral['id']}))
                                            )
        else:
            mineral_names_ids[letter] = [
                                         (mineral['name'],
                                         reverse('minerals:detail', kwargs={"pk": mineral['id']}))
                                        ]
    return mineral_names_ids

@register.filter('concatenate')
def concatenate(arg1, arg2):
    """concatenate"""
    return str(arg1) + str(arg2)
