from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CriarUsuarioForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm



# Create your views here
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def image_view(request):
    return render(request, 'home.html', {})


def contato_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})


def login_usuario_view(request):
    if request.user.is_authenticated:
        return redirect('paginas:painel')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('paginas:painel')

            else:
                messages.info(request, "Usuário ou senha incorretos!")

        context = {}
        return render(request, 'login_usuario.html', context)


@login_required(login_url='paginas:login')
def painelUsuario(request):
    return render(request, 'painel_usuario.html', {})


@login_required(login_url='paginas:login')
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


@login_required(login_url='paginas:login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Sua senha foi atualizada com sucesso!')
            return redirect('paginas:painel')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'alterar_senha.html', {
        'form': form
    })


@login_required(login_url='paginas:login')
def menuFuncionario(request):
    return render(request, 'menu_rh.html', {})


@login_required(login_url='paginas:login')
def menuProcesso(request):
    return render(request, 'menu_processo.html', {})