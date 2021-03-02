from django.urls import path
from .views import (
    solicitacao_create_view
)

app_name = 'solicitacoes'
urlpatterns = [
    path('', solicitacao_create_view, name='solicitacao_home'),
    path('create/', solicitacao_create_view, name='criar_solicitacao'),
]