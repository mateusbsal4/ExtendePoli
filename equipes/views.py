from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Equipe, Membro
from .forms import EquipeForm, MembroForm
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

def create_membro(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)
    if request.method == 'POST':
        form = MembroForm(request.POST)
        if form.is_valid():
            membro_nome = form.cleaned_data['nome']
            membro_curso = form.cleaned_data['curso']
            ano_entrada = form.cleaned_data['entrada_equipe']
            membro = Membro(nome=membro_nome,
                            curso=membro_curso,
                            entrada_equipe = ano_entrada,
                            )
            membro.save()
            membro.equipes.add(equipe)
            return HttpResponseRedirect(
                reverse('equipes:detail', args=(equipe_id, )))
    else:
        form = MembroForm()
    context = {'form': form, 'equipe': equipe}
    return render(request, 'equipes/membro.html', context)

