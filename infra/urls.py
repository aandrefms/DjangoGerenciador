from django.urls import path
from .views import (
    processo_create_view,
    func_view
)

app_name = 'infra'
urlpatterns = [
    path('', func_view, name='func'),   #coloquei o as_view() para poder funcionar como uma view
    path('/<int:my_id>/', processo_create_view, name='func'),
]