from django import forms
from .models import Solicitacao, SolicitacaoSearch
from django.forms import ClearableFileInput

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = '__all__'

        widgets = {'detalhes': forms.Textarea(attrs={}),
                   'local': forms.Textarea(attrs={}),
                   }

class SolicitacaoSearchForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoSearch
        fields = '__all__'
        widgets = {'detalhes': forms.Textarea(attrs={}),
                   'local': forms.Textarea(attrs={}),
                   }