from django.shortcuts import render, get_object_or_404, redirect
from .forms import SolicitacaoForm, SolicitacaoSearchForm
from .models import Solicitacao
from django.contrib.auth.decorators import login_required
from .choices import *
# Create your views here.
query = None


def get_servico(item):
    for i in SERVICOS:
        for element in i[1]:
            if item == element[0]:
                return str(i[0])


def solicitacao_create_view(request):
    if request.method == 'POST':
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
    global query
    if query == None:
        queryset = Solicitacao.objects.all()
    else:
        queryset = query
    query = None
    context = {
        "object_list": queryset
    }
    return render(request, "solicitacoes/solicitacao_list.html", context)


@login_required(login_url="paginas:login")
def solicitacao_search(request):
    global query
    if request.method == 'POST':
        form = SolicitacaoSearchForm(request.POST)
        if form.is_valid():
            queryset = Solicitacao.objects.all()
            if request.POST.get('servicos'):
                queryset = queryset.filter(servicos=request.POST['servicos'])
            if request.POST.get('periodo'):
                queryset = queryset.filter(periodo=request.POST['periodo'])
            if request.POST.get('tipo_solicitacao'):
                queryset = queryset.filter(tipo_solicitacao=request.POST['tipo_solicitacao'])
            if request.POST.get('turno'):
                queryset = queryset.filter(turno=request.POST['turno'])
            query = queryset
            return redirect('solicitacoes:lista_solicitacao')
        else:
            print(form.errors)
    else:
        form = SolicitacaoSearchForm()
    context = {
        "form": form
    }
    return render(request, "solicitacoes/solicitacao_search.html", context)