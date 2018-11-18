from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Mineral


def index(request):
    """Returns the main page with default of minerals starting with A listed."""
    minerals = Mineral.objects.filter(name__startswith='A')
    messages.success(request, "Successfully found {} of the following minerals!".format(len(minerals)))
    return render(request, 'index.html', {'minerals': minerals})


def mineral_detail(request, pk):
    """Get the details of the selected mineral from the user.
    Additional query to get a random mineral. Will be better for the DB than a select all."""
    selected_mineral = get_object_or_404(Mineral, id=pk)
    return render(request,
                  'detail.html',
                  {'mineral': selected_mineral})


def search_by_name(request):
    """Returns an index view with only the minerals displayed which meet the query criteria."""
    search_term = request.GET.get('q')
    minerals = Mineral.objects.filter(name__icontains=search_term)
    messages.success(request, "Successfully found {} of the following minerals!".format(len(minerals)))
    return render(request, 'index.html', {'minerals': minerals})


def search_by_mineral_first(request, letter=None):
    if letter:
        minerals = Mineral.objects.filter(name__startswith=letter)
    else:
        minerals = Mineral.objects.filter(name__startswith='A')
    messages.success(request, "Successfully found {} of the following minerals!".format(len(minerals)))
    return render(request, 'index.html', {'minerals': minerals})