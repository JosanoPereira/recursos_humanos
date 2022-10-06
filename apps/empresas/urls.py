from django.urls import path
from .views import EmpresaCreate, EmpresaUpdate

urlpatterns = [
    path('empresa_create/', EmpresaCreate.as_view(), name='empresaCreate'),
    path('empresa_update/<int:pk>', EmpresaUpdate.as_view(), name='empresaUpdate'),
]