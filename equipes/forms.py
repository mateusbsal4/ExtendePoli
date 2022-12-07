from django.forms import ModelForm
from django import forms
from .models import Equipe, Membro, Foto, Evento

class DateInput(forms.DateInput):
    input_type = 'date'
    
class EquipeForm(ModelForm):
    class Meta:
        model = Equipe
        fields = [
            'nome',
            'logo',
            'descricao',
        ]
        labels = {
            'nome': 'Nome',
            'logo': 'Url do logo',
            'descricao': 'Descrição',
        }

class MembroForm(ModelForm):
    class Meta:
        model = Membro
        fields = [
            'nome',
            'curso',
            'entrada_equipe',
        ]
        labels = {
            'nome': 'Nome',
            'curso': 'Curso de ingresso na Poli',
            'entrada_equipe': "Data de entrada na equipe",         
        }
        widgets = {
            'entrada_equipe': DateInput(),
        }
class FotoForm(ModelForm):
    class Meta:
        model = Foto
        fields = [
            'link',
        ]
        labels = {
            'link': 'Url da foto',
        }


    
class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = [
            # 'ID',
            'nome',
            'data',
            'tipo',
            'descricao',
        ]
        widgets = {
            'data': DateInput(),
        }
        labels = {
            # 'ID':'ID',
            'nome': 'Nome',
            'data': 'Data',
            'tipo': 'Tipo',
            'descricao': 'Descrição',       
        }

class DelEventoForm(forms.Form):
    ID = forms.IntegerField()