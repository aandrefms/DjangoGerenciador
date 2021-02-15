from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProcessoForm, DocumentoForm, FilterProcessoForm
from .models import Processo, Documento, FilterProcesso, User
from django.contrib.auth.decorators import login_required

item = None
item_group = None
queryset_search = []
# Create your views here.
@login_required(login_url='paginas:login')
def processo_create_view(request):
    usuario = request.user.first_name
    if request.method == 'POST':
        update_request = request.POST.copy()
        update_request.update({'responsavel': request.user.id})
        my_form = ProcessoForm(update_request)
        #my_form = ProcessoForm(request.POST, request.FILES)
        '''my_form.fields['responsavel'].choices = [(usuario, usuario)]
        my_form.fields['responsavel'].initial = [0]'''
        if my_form.is_valid():
            # now the data is good
            my_form.fields['responsavel'].initial = request.user
            print(my_form.cleaned_data)
            '''item = my_form.cleaned_data['origem_processo']
            id = Processo.objects.get(origem_processo=item).id'''
            print(id)
            # form_file.fields["processo"] = 'testando'
            my_form.save()
            # Processo.objects.create(**my_form.cleaned_data)
            return redirect('infra:lista_processos')
        else:
            print(my_form.errors)
    else:
        my_form = ProcessoForm()
        my_form.fields['responsavel'].choices = [(usuario, usuario)]
        my_form.fields['responsavel'].initial = [0]
    context = {
        'form': my_form
    }
    return render(request, "infra/processo_create.html", context)

@login_required(login_url='paginas:login')
def processo_search1(request):
    global queryset_search
    if request.method == 'POST':
        search_form = FilterProcessoForm(request.POST)
        if search_form.is_valid():
            """query = search_form.cleaned_data
            queryset = Processo.objects
            if query['unique_id'] != '':
                queryset = queryset.filter(unique_id=query['unique_id'])
            elif query['origem_processo'] != '':
                queryset = queryset.filter(origem_processo=query['origem_processo'])
            elif query['tipo_processo'] != '':
                queryset = queryset.filter(tipo_processo=query['tipo_processo'])
            elif query['assunto_detalhado'] != '':
                queryset = queryset.filter(assunto_detalhado=query['assunto_detalhado'])
            elif query['responsavel'] != '':
                nome = User.objects.get(username=query['responsavel'])
                queryset = queryset.filter(responsavel=nome)
            else:
                queryset = ''"""

            filters = {
                key: value
                for key, value in request.POST.items()
                if key in ['origem_processo', 'tipo_processo',
                           'assunto_detalhado']
            }

            queryset_search = Processo.objects.filter(**filters)
            return redirect('infra:lista_processos')
    else:
        search_form = FilterProcessoForm()

    context = {
        'form': search_form
    }
    return render(request, "infra/processo_search.html", context)



@login_required(login_url='paginas:login')
def processo_search(request):
    global item, item_group
    if request.method == 'POST':
        search_form = FilterProcessoForm(request.POST)
        if search_form.is_valid():
            item = search_form.cleaned_data['search']
            item_group = search_form.cleaned_data['filter_field']
            return redirect('infra:lista_processos')
    else:
        search_form = FilterProcessoForm()

    context = {
        'form': search_form
    }
    return render(request, "infra/processo_search.html", context)

@login_required(login_url='paginas:login')
def processo_view(request, *args, **kwargs):
    return render(request, 'infra/home.html', {})

@login_required(login_url='paginas:login')
def processo_detalhes(request, my_id):
    obj = get_object_or_404(Processo, id=my_id)
    """if request.method == 'POST':
        # confirmando se quer deletar
        obj.delete()
        return redirect('../../')"""
    context = {
        'objeto': obj
    }
    return render(request, "infra/processo_detalhes.html", context)

@login_required(login_url='paginas:login')
def processo_list(request):
    global queryset_search
    """global item, item_group
    if item is None:
        queryset = Processo.objects.all()
    elif item_group == 'NATUREZA_PROCESSO':
        queryset = Processo.objects.filter(NATUREZA_PROCESSO=item)
    elif item_group == 'unique_id':
        queryset = Processo.objects.filter(unique_id=item)
    elif item_group == 'origem_processo':
        queryset = Processo.objects.filter(origem_processo=item)
    elif item_group == 'tipo_processo':
        queryset = Processo.objects.filter(tipo_processo=item)
    elif item_group == 'natureza_processo':
        queryset = Processo.objects.filter(natureza_processo=item)
    else:
        queryset = Processo.objects.filter(responsavel=item)
    item_group = None
    item = None"""
    if queryset_search == []:
        queryset = Processo.objects.all()
    else:
        queryset = queryset_search
        queryset_search = []
        # queryset = Processo.objects.filter(NATUREZA_PROCESSO='OSTENSIVO')
    context = {
        "object_list": queryset
    }
    return render(request, "infra/processo_list.html", context)


@login_required(login_url='paginas:login')
def processo_editar(request, pk):
    processo = Processo.objects.get(id=pk)
    form = ProcessoForm(instance=processo)
    if request.method == 'POST':

        form = ProcessoForm(request.POST, request.FILES, instance=processo)
        if form.is_valid():
            # now the data is good
            # print(my_form.cleaned_data)
            '''b = Processo.concatPdf(file=str(form.cleaned_data['documentos']))
            form.cleaned_data['documentos'] = b'''
            form.save()
            # Processo.objects.create(**my_form.cleaned_data)
            return redirect('infra:lista_processos')
    context = {'form':form}
    return render (request, "infra/processo_editar.html", context)


@login_required(login_url='paginas:login')
def documento_insert(request, pk):
    queryset1 = Processo.objects.get(id=pk)
    queryset = pk
    if request.method == 'POST':
        #form_file = DocumentoForm(request.POST, request.FILES)
        """form_file.fields['processo'].choices = [(queryset, queryset)]
        form_file.fields['processo'].initial = [0]"""
        update_request = request.POST.copy()
        update_request.update({'processo': queryset1})
        form_file = DocumentoForm(update_request, request.FILES)
        if form_file.is_valid():
            form_file.save()
            return redirect('infra:lista_processos')
        else:
            print(form_file.errors)
    else:
        form_file = DocumentoForm()
        form_file.fields['processo'].choices = [(queryset, queryset)]
        form_file.fields['processo'].initial = [0]
        # form_file.fields["processo"] = 'testando'
    context = {
        'test': form_file
    }
    return render(request, "infra/documento_inserir.html", context)


@login_required(login_url='paginas:login')
def documento_list(request, pk):
    querydoc = Processo.objects.get(id=pk)
    querydoc = querydoc.processo.all()
    context = {
        "object_list": querydoc
    }
    return render(request, "infra/documento_list.html", context)



