from django.db import models
from apps.funcionarios.models import Funcionario
from django.urls import reverse_lazy


class Documento(models.Model):
    num_doc = models.CharField(max_length=14)
    dono = models.ForeignKey(Funcionario, on_delete=models.PROTECT, verbose_name='Proprietário do Documento')
    arquivo = models.FileField(upload_to='documentos')

    def __str__(self):
        return self.num_doc

