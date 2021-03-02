from django.shortcuts import render, get_object_or_404, redirect
from .forms import SolicitacaoForm
from .models import Solicitacao
from django.contrib.auth.decorators import login_required
# Create your views here.

def solicitacao_create_view(request):
    if request.method == 'POST':
        form = SolicitacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rh:rh_home')
        else:
            print(form.errors)
    else:
        form = SolicitacaoForm()
    context = {
        'form': form
    }
    return render(request, "solicitacoes/solicitacao_create.html", context)