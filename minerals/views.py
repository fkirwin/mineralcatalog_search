from django.shortcuts import render

# Create your views here.
import random

from django.shortcuts import render, get_object_or_404
from django.core.exceptions import EmptyResultSet, ObjectDoesNotExist

from .models import Mineral

def index(request):
    """Returns the main page with all of the minerals listed."""
    minerals = Mineral.objects.all()
    return render(request, 'index.html', {'minerals': minerals})

def mineral_detail(request, pk):
    """Get the details of the selected mineral from the user.
    Additional query to get a random mineral. Will be better for the DB than a select all."""
    selected_mineral = get_object_or_404(Mineral, id=pk)
    return render(request,
                  'detail.html',
                  {'mineral': selected_mineral})

def search_by_name(request):
    search_term = request.GET.get('q')
    minerals = Mineral.objects.filter(name__icontains=search_term)
    return render(request, 'index.html', {'minerals': minerals})