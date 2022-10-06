from django.urls import path
from .views import FuncionarioList, FuncionarioUpdate,\
    FuncionarioDelete, FuncionarioCreate

urlpatterns = [
    path('', FuncionarioList.as_view(), name='list_funcionario'),
    path('update/<int:pk>/', FuncionarioUpdate.as_view(), name='update_funcionario'),
    path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('create/', FuncionarioCreate.as_view(), name='create_funcionario'),
]
