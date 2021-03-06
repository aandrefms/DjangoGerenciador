from django.urls import path
from .views import (
    processo_create_view,
    processo_detalhes,
    processo_view,
    processo_list,
    processo_editar,
    processo_search1,
    documento_insert,
    documento_list,
    register_despatch
)

app_name = 'infra'
urlpatterns = [
    path('', processo_view, name='func'),
    path('processos/create', processo_create_view, name='criar_processo'),   #coloquei o as_view() para poder funcionar como uma view
    path('processos/<int:my_id>/', processo_detalhes, name='detalhes_processos'),
    path('processos/', processo_list, name='lista_processos'),
    path('processos/<int:pk>/editar', processo_editar, name='editar_processo'),
    path('processos/search', processo_search1, name='search_processo'),
    path('processos/<int:pk>/inserirdocumento', documento_insert, name='inserir_documento'),
    path('processos/<int:pk>/documentos', documento_list, name='lista_documentos'),
    path('processos/<int:pk>/despatch', register_despatch, name='register_despatch')
]