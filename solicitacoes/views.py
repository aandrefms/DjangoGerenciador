from django.shortcuts import render, get_object_or_404, redirect
from .forms import SolicitacaoForm
from .models import Solicitacao
from django.contrib.auth.decorators import login_required
from .choices import *
# Create your views here.

def get_servico(item):
    for i in SERVICOS:
        for element in i[1]:
            if item == element[0]:
                return str(i[0])


def solicitacao_create_view(request):
    if request.method == 'POST':
        """update_request = 
        my_form = SolicitacaoForm(request.POST)
        # form = SolicitacaoForm(request.POST)
        item = my_form.cleaned_data['tipo_servico']
        item = get_servico(item)
        update_request.update({'servico': item})
        form = SolicitacaoForm(update_request)"""
        form = request.POST.copy()
        item = request.POST.get('tipo_servico')

        # item = form.cleaned_data['tipo_servico']
        item1 = get_servico(item)
        print('ASDUAHSDIUASHDIUAS' + item1)
        form.update({'servicos': item1})
        form = SolicitacaoForm(form)
        if form.is_valid():

            form.save()
            return redirect('solicitacoes:lista_solicitacao')
        else:
            print(form.errors)
    else:
        form = SolicitacaoForm()
    context = {
        'form': form
    }
    return render(request, "solicitacoes/solicitacao_create.html", context)


@login_required(login_url="paginas:login")
def solicitacao_list(request):

    queryset = Solicitacao.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "solicitacoes/solicitacao_list.html", context)