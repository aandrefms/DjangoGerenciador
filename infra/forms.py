from django import forms
from .models import Processo
from django.forms import ClearableFileInput

class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processo
        fields = ('origem_processo', 'tipo_processo', 'assunto_detalhado', 'natureza_processo', 'observacao',
                  'documentos')  # Preciso colocar 'imagens' aqui caso eu insira o campo imagens
        # fields = '__all__'

        widgets = {
            'documentos': ClearableFileInput(attrs={'multiple': True}),
        }

