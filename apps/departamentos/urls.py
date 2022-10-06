from django.urls import path
from .views import DepartamentoList, DepartamentoUpdate, \
    DepartamentoDelete, DepartamentoCreate

urlpatterns = [
    path('', DepartamentoList.as_view(), name='list_departamento'),
    path('create/', DepartamentoCreate.as_view(), name='create_departamento'),
    path('update/<int:pk>', DepartamentoUpdate.as_view(), name='update_departamento'),
    path('delete/<int:pk>', DepartamentoDelete.as_view(), name='delete_departamento'),
]
