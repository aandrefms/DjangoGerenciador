from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProcessoForm
from .models import Processo
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
def func_view(request, *args, **kwargs):
    return render(request, 'infra/home.html', {})

@login_required(login_url='paginas:login')
def processo_view(request, my_id):
    obj = get_object_or_404(Processo, id=my_id)
    if request.method == 'POST':
        # confirmando se quer deletar
        obj.delete()
        return redirect('../../')
    context = {
        'objeto': obj
    }
    return render(request, "infra/processo_detalhes.html", context)

@login_required(login_url='paginas:login')
def processo_list(request):
    queryset = Processo.objects.all()
    context = {
        "object_list" : queryset
    }
    return render(request, "infra/processo_list.html", context)