from django.urls import path
from .views import (
    funcionario_create_view,
    funcionario_view,
    funcionario_detalhes,
    funcionario_list,
    funcionario_editar
)

app_name = 'rh'
urlpatterns = [
    path('', funcionario_view, name='rh_home'),
    path('funcionarios/create/', funcionario_create_view, name='criar_funcionario'),
    path('funcionarios/<int:pk>/', funcionario_detalhes, name='detalhes_funcionario'),
    path('funcionarios/', funcionario_list, name='lista_funcionario'),
    path('funcionarios/<int:pk>/editar', funcionario_editar, name='editar_funcionario')
]