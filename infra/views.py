from django.shortcuts import render
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