from django.forms import ModelForm
from .models import Equipe

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

