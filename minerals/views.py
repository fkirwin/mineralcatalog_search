from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Mineral


def index(request):
    """Returns the main page with all of the minerals listed."""
    minerals = Mineral.objects.all()
    messages.success(request, "Check out all these minerals!")
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
