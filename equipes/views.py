from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Equipe
# Create your views here.

def list_equipes(request):
    equipe_list = Equipe.objects.all()
    context = {'equipe_list': equipe_list}
    return render(request, 'equipes/index.html', context)

def detail_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)
    context = {'equipe': equipe}
    return render(request, 'equipes/detail.html', context)


def create_equipe(request):
    if request.method == 'POST':
        equipe_nome = request.POST['nome']
        equipe_descricao = request.POST['descricao']
        equipe_logo = request.POST['logo']
        equipe = Equipe(nome=equipe_nome,
                      descricao=equipe_descricao,
                      logo=equipe_logo)
        equipe.save()
        return HttpResponseRedirect(
            reverse('equipes:detail', args=(equipe.id, )))
    else:
        return render(request, 'equipes/create.html', {})

def update_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)

    if request.method == "POST":
        equipe.nome = request.POST['nome']
        equipe.descricao = request.POST['descricao']
        equipe.logo = request.POST['logo']
        equipe.save()
        return HttpResponseRedirect(
            reverse('equipes:detail', args=(equipe.id, )))

    context = {'equipe': equipe}
    return render(request, 'equipes/update.html', context)



def delete_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)

    if request.method == "POST":
        equipe.delete()
        return HttpResponseRedirect(reverse('equipes:index'))

    context = {'equipe': equipe}
    return render(request, 'equipes/delete.html', context)


