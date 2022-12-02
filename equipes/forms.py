from django.forms import ModelForm
from .models import Equipe, Membro, Foto

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

class FotoForm(ModelForm):
    class Meta:
        model = Foto
        fields = [
            'link',
        ]
        labels = {
            'link': 'Url da foto',
        }