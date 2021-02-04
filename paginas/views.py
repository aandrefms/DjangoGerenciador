from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CriarUsuarioForm

# Create your views here
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def contato_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})


def login_usuario_view(request, *args, **kwargs):
    return render(request, 'login_usuario.html', {})

def criar_funcionario_view(request):
    form = CriarUsuarioForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, 'criar_usuario.html', context)