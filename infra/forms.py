from django import forms
from .models import Processo, Documento, FilterProcesso
from django.forms import ClearableFileInput

class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processo
        fields = ('origem_processo', 'tipo_processo', 'assunto_detalhado', 'natureza_processo',
                  'observacao', 'responsavel')  # Preciso colocar 'imagens' aqui caso eu insira o campo imagens
        # fields = '__all__'

        '''widgets = {
            'documentos': ClearableFileInput(attrs={'multiple': True}),
        }
'''

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'

        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True})
        }

class FilterProcessoForm(forms.ModelForm):
    class Meta:
        model = FilterProcesso
        fields = '__all__'

