from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProcessoForm, DocumentoForm
from .models import Processo, Documento
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='paginas:login')
def processo_create_view(request):
    my_form = ProcessoForm()
    if request.method == 'POST':
        my_form = ProcessoForm(request.POST, request.FILES)
        if my_form.is_valid():
            # now the data is good
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
    context = {
        'form': my_form
    }
    return render(request, "infra/processo_create.html", context)


@login_required(login_url='paginas:login')
def documento_insert(request, pk):
    queryset = Processo.objects.get(id=pk)
    queryset = queryset.origem_processo
    form_file = DocumentoForm()
    if request.method == 'POST':
        form_file = DocumentoForm(request.POST, request.FILES)
        form_file.fields['processo'].choices = [(queryset, queryset)]
        form_file.fields['processo'].initial = [0]
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
        'test':form_file
    }
    return render(request, "infra/documento_inserir.html", context)

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
    queryset = Processo.objects.all()
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
            b = Processo.concatPdf(file=str(form.cleaned_data['documentos']))
            form.cleaned_data['documentos'] = b
            form.save()
            # Processo.objects.create(**my_form.cleaned_data)
            return redirect('infra:lista_processos')
    context = {'form':form}
    return render (request, "infra/processo_editar.html", context)