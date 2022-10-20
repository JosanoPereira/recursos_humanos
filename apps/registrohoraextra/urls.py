from django.urls import path
from .views import HoraList, HoraUpdate, HoraCreate, HoraDelete, Utitizou_hora_extra

urlpatterns = [
    path('', HoraList.as_view(), name='list_hora_extra'),
    path('create/', HoraCreate.as_view(), name='create_hora_extra'),
    path('update/<int:pk>', HoraUpdate.as_view(), name='update_hora_extra'),
    path('utilizou_hora_extra/<int:pk>', Utitizou_hora_extra.as_view(), name='hora_usada'),
    path('update_funcionario/<int:pk>', HoraUpdate.as_view(), name='update_hora_extra_funcionario'),
    path('delete/<int:pk>', HoraDelete.as_view(), name='delete_hora_extra'),
]
