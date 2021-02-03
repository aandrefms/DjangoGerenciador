from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProcessoForm
from .models import Processo

# Create your views here.
def processo_create_view(request, *args, **kwargs):
    my_form = ProcessoForm()
    if request.method == 'POST':
        my_form = ProcessoForm(request.POST)
        if my_form.is_valid():
            # now the data is good
            print(my_form.cleaned_data)
            Processo.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }
    return render(request, "infra/home.html", context)

def func_view(request, *args, **kwargs):
    return render(request, 'infra/home.html', {})

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

def processo_list(request):
    queryset = Processo.objects.all()
    context = {
        "object_list" : queryset
    }
    return render(request, "infra/processo_lista.html", context)