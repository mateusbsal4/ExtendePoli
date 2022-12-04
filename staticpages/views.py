from django.shortcuts import render

import sys
sys.path.append('../')
from equipes.views import Evento, get_events



import json

def index(request):
    eve = get_events()
    context = {'eve':eve}
    return render(request, 'staticpages/index.html', context)


def about(request):
    context = {}
    return render(request, 'staticpages/about.html', context)

