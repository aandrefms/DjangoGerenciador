from django import forms
from .models import Processo


class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processo
        fields = ('origem_processo', 'tipo_processo', 'assunto_detalhado', 'natureza_processo', 'observacao',
                  'documentos')  # Preciso colocar 'imagens' aqui caso eu insira o campo imagens

    '''origem_processo = forms.CharField(label='Origem do Processo', widget=forms.TextInput(attrs={
                                                                'placeholder' : 'Origem do Processo'
                                                            }))
    tipo_processo = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Descricao',
        "class": "new_class_2",
        "id": 'my-id',
        "rows": 20,
        "cols": 20}))
    assunto_detalhado = forms.CharField(max_length=900)
    natureza_processo = forms.CharField(max_length=120, initial='OSTENSIVO')
    observacao = forms.CharField(max_length=120)
'''
