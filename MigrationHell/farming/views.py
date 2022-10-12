from django.shortcuts import render
from django.http import HttpResponse

from .models import Farmer

def index(request):
    farms = Farmer.objects.order_by('name')
    output = '\n'.join([farm.name for farm in farms])
    return HttpResponse(output)

def home(request):
    farmers = Farmer.objects.order_by('name')
    context = {
        'farmers': farmers
    }
    # render takes request, location of html, and context as arguments
    return render(request, 'farming/home.html', context)