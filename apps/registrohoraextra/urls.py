from django.urls import path
from .views import HoraList, HoraUpdate, HoraCreate, HoraDelete, UtitizouHoraExtra, RelatorioCSV

urlpatterns = [
    path('', HoraList.as_view(), name='list_hora_extra'),
    path('create/', HoraCreate.as_view(), name='create_hora_extra'),
    path('update/<int:pk>', HoraUpdate.as_view(), name='update_hora_extra'),
    path('utilizou-hora-extra/<int:pk>',
         UtitizouHoraExtra.as_view(), name='utitizou_hora_extra'),
    path('update_funcionario/<int:pk>', HoraUpdate.as_view(), name='update_hora_extra_funcionario'),
    path('delete/<int:pk>', HoraDelete.as_view(), name='delete_hora_extra'),
    path('relatorio_csv', RelatorioCSV.as_view(), name='relatorio_csv'),
]
