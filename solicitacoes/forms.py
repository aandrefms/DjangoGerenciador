from django import forms
from .models import Solicitacao
from django.forms import ClearableFileInput

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = '__all__'

        widgets = {'detalhes': forms.Textarea(attrs={}),
                   'local': forms.Textarea(attrs={}),
                   }