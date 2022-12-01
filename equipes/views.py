from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Equipe
from .forms import EquipeForm
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
        form = EquipeForm(request.POST)
        if form.is_valid():
            equipe_nome = form.cleaned_data['nome']
            equipe_descricao = form.cleaned_data['descricao']
            equipe_logo = form.cleaned_data['logo']
            equipe = Equipe(nome=equipe_nome,
                          descricao=equipe_descricao,
                          logo=equipe_logo)
            equipe.save()
            return HttpResponseRedirect(
                reverse('equipes:detail', args=(equipe.id, )))
    else:
        form = EquipeForm()
    context = {'form': form}
    return render(request, 'equipes/create.html', context)



def update_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)

    if request.method == "POST":
        form = EquipeForm(request.POST)
        if form.is_valid():
            equipe_nome = form.cleaned_data['nome']
            equipe_descricao = form.cleaned_data['descricao']
            equipe_logo = form.cleaned_data['logo']
            equipe.save()
            return HttpResponseRedirect(
                reverse('equipes:detail', args=(equipe.id, )))
    else:
        form = EquipeForm(
            initial={
                'nome': equipe.nome,
                'logo': equipe.logo,
                'descricao': equipe.descricao
            })

    context = {'equipe': equipe, 'form': form}
    return render(request, 'equipes/update.html', context)



def delete_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)

    if request.method == "POST":
        equipe.delete()
        return HttpResponseRedirect(reverse('equipes:index'))

    context = {'equipe': equipe}
    return render(request, 'equipes/delete.html', context)

def delete_post(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)

    if request.method == "POST":
        equipe.delete()
        return HttpResponseRedirect(reverse('equipes:index'))

    context = {'equipe': equipe}
    return render(request, 'equipes/delete.html', context)



