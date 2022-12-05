from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from .models import Equipe, Membro, Foto, Evento
from .forms import EquipeForm, MembroForm, FotoForm, EventoForm, DelEventoForm
from django.contrib.auth.decorators import login_required, permission_required
import json
# Create your views here.

def list_equipes(request):
    equipe_list = Equipe.objects.all()
    context = {'equipe_list': equipe_list}
    return render(request, 'equipes/index.html', context)

def detail_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)

    eve = get_events(equipe_id)
    context = {'equipe': equipe, 'eve':eve}
    return render(request, 'equipes/detail.html', context)

@login_required
@permission_required('equipes.add_equipe')
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


@login_required
@permission_required('equipes.change_equipe')
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


@login_required
@permission_required('equipes.delete_equipe')
def delete_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)

    if request.method == "POST":
        equipe.delete()
        return HttpResponseRedirect(reverse('equipes:index'))

    context = {'equipe': equipe}
    return render(request, 'equipes/delete.html', context)

@login_required
@permission_required('equipes.change_equipe')
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

@login_required
@permission_required('equipes.change_equipe')
def delete_membro(request, membro_id):
    membro = get_object_or_404(Membro, pk=membro_id)

    if request.method == "POST":
        membro.delete()
        return HttpResponseRedirect(reverse('equipes:index' ))

    context = {'membro': membro}
    return render(request, 'equipes/delete_membro.html', context)

@login_required
@permission_required('equipes.change_equipe')
def create_foto(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)
    if request.method == 'POST':
        form = FotoForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            foto = Foto(link = link,
                        equipe = equipe)
            foto.save()
            return HttpResponseRedirect(
                reverse('equipes:detail', args=(equipe_id, )))
    else:
        form = FotoForm()
    context = {'form': form, 'equipe': equipe}
    return render(request, 'equipes/foto.html', context)




@login_required
@permission_required('equipes.change_equipe')
def edit_evento(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)
    form1 = EventoForm()
    form2 = DelEventoForm()
    if request.method == 'POST' and 'btnform1' in request.POST:
        form1 = EventoForm(request.POST)
        if form1.is_valid():
            # eve_id = form.cleaned_data['ID']
            eve_name = form1.cleaned_data['nome']
            eve_desc = form1.cleaned_data['descricao']
            eve_date = form1.cleaned_data['data']
            eve_type = form1.cleaned_data['tipo']
            evento = Evento(
                            # ID=eve_id,
                            nome=eve_name,
                            descricao = eve_desc,
                            data = eve_date,
                            tipo = eve_type,
                            equipe=equipe,
                            )
            evento.save()
            # evento.equipes.add(equipe)
            # return HttpResponseRedirect(
            #     reverse('equipes:detail', args=(equipe_id, )))
    if request.method == 'POST' and 'btnform2' in request.POST:
        form2 = DelEventoForm(request.POST)
        if form2.is_valid():
            eve_id = form2.cleaned_data['ID']
            evento = get_object_or_404(Evento, pk=eve_id)
            evento.delete()
            # return HttpResponseRedirect(
            #         reverse('equipes:detail', args=(equipe_id, )))
    
    eve = get_events(equipe_id)
    context = {'form1':form1,'form2':form2, 'equipe': equipe, 'eve':eve}
    return render(request, 'equipes/evento.html', context)
    

@login_required
@permission_required('equipes.change_equipe')
def delete_evento(request, membro_id):
    membro = get_object_or_404(Membro, pk=membro_id)

    if request.method == "POST":
        membro.delete()
        return HttpResponseRedirect(reverse('equipes:index' ))

    context = {'membro': membro}
    return render(request, 'equipes/delete_membro.html', context)



def get_events(*equipe_id):
    if equipe_id:
        eventos = Evento.objects.filter(equipe_id=equipe_id)
    else:
        eventos = Evento.objects.all()

    listaEventos = []
    for x in eventos:
        listaEventos.append(
            {
                "id": x.id,
                "name": x.nome,
                "description": x.descricao,
                "date" : x.data.strftime("%m/%d/%Y"),
                "type" : x.tipo,
            }
        )
        # print(x.data.strftime("%m/%d/%Y"))
        
    return json.dumps(listaEventos,indent=2)