from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CriarUsuarioForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# Create your views here
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def image_view(request):
    return render(request, 'home.html', {})


def contato_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})


def login_usuario_view(request):
    if request.user.is_authenticated:
        return redirect('infra:func')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('infra:func')

            else:
                messages.info(request, "Usuário ou senha incorretos!")

        context = {}
        return render(request, 'login_usuario.html', context)


def logoutUser(request):
    logout(request)
    return redirect('paginas:home')

def criar_funcionario_view(request):
    if request.user.is_authenticated:
        return redirect('infra:func')
    else:
        if request.method == 'POST':
            form = CriarUsuarioForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f"Usuário {user} foi criado com sucesso")
                return redirect('paginas:login')
        else:
            form = CriarUsuarioForm()
        context = {
            'form': form
        }
        return render(request, 'criar_usuario.html', context)