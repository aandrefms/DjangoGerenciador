from django.urls import path
from .views import (
    processo_create_view,
    func_view,
    processo_view,
    processo_list,
    processo_editar
)

app_name = 'infra'
urlpatterns = [
    path('', func_view, name='func'),
    path('processos/create', processo_create_view, name='criar_processo'),   #coloquei o as_view() para poder funcionar como uma view
    path('processos/<int:my_id>/', processo_view, name='detalhes_processos'),
    path('processos/', processo_list, name='lista_processos'),
    path('processo/<int:pk>/editar', processo_editar, name='editar_processo')
]