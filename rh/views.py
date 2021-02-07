from django.shortcuts import render, get_object_or_404, redirect
from .forms import FuncionarioForm
from .models import Funcionario
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='paginas:login')
def funcionario_create_view(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('rh:rh_home')
        else:
            print(form.errors)
    else:
        form = FuncionarioForm()
    context = {
        'form': form
    }
    return render(request, "rh/funcionario_create.html", context)

@login_required(login_url='paginas:login')
def funcionario_view(request):
    return render(request, 'rh/home.html')


@login_required(login_url='paginas:login')
def funcionario_detalhes(request, pk):
    obj = get_object_or_404(Funcionario, id=pk)
    if request.method == 'POST':
        """if request.method == 'POST':
                # confirmando se quer deletar
                obj.delete()
                return redirect('../../')"""
    context = {
        'objeto':obj
    }
    return render(request, "rh/funcionario_detalhes.html", context)


@login_required(login_url="paginas:login")
def funcionario_list(request):
    queryset = Funcionario.objects.all
    context = {
        "object_list": queryset
    }
    return render(request, "rh/funcionario_list.html", context)


@login_required(login_url="paginas:login")
def funcionario_editar(request, pk):
    funcionario = Funcionario.objects.get(id=pk)
    form = FuncionarioForm(instance=funcionario)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, request.FILES, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('rh:lista_funcionario')
    context = {'form': form}
    return render(request, 'rh/funcionario_editar.html', context)