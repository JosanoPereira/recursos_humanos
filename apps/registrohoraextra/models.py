from django.db import models
from django.urls import reverse_lazy, reverse

from apps.funcionarios.models import Funcionario


# TODO Mudar para ter duas chamadas diferentes em views diferentes
class HoraExtra(models.Model):
    motivo = models.CharField(max_length=200)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)
    utilizada = models.BooleanField(default=False)

    def __str__(self):
        return self.motivo

    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self.funcionario.id])