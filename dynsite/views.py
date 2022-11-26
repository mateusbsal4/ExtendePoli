from django.shortcuts import render, get_object_or_404
from .models import Equipe
# Create your views here.

def list_equipes(request):
    equipe_list = Equipe.objects.all()
    context = {'equipe_list': equipe_list}
    return render(request, 'dynsite/index.html', context)

def detail_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)
    context = {'equipe': equipe}
    return render(request, 'dynsite/detail.html', context)