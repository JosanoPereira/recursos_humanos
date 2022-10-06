from django.db import models
from apps.funcionarios.models import Funcionario


class HoraExtra(models.Model):
    motivo = models.CharField(max_length=200)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.motivo
