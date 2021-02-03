from django.urls import path
from .views import (
    processo_create_view,
    func_view,
    processo_view,
    processo_list
)

app_name = 'infra'
urlpatterns = [
    path('', func_view, name='func'),   #coloquei o as_view() para poder funcionar como uma view
    path('/processos/<int:my_id>/', processo_view, name='detalhes_processos'),
    path('/processos/', processo_list, name='lista_processos')
]