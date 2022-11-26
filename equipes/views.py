from django.shortcuts import render, get_object_or_404
from .models import Equipe
# Create your views here.

def list_equipes(request):
    equipe_list = Equipe.objects.all()
    context = {'equipe_list': equipe_list}
    return render(request, 'equipes/index.html', context)

def detail_equipe(request, equipe_nome):
    equipe = get_object_or_404(Equipe, nome=equipe_nome)
    context = {'equipe': equipe}
    return render(request, 'equipes/detail.html', context)