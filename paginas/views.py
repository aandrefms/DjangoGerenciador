from django.shortcuts import render
from django.shortcuts import render


# Create your views here
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def contato_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})


def area_funcionario_view(request, *args, **kwargs):
    return render(request, 'area_funcionario.html', {})