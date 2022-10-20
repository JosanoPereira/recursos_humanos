from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse_lazy

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=150, help_text='Nome do Funcionário')
    user = models.OneToOneField(User, on_delete=models.PROTECT, unique=True)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT,
                                null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('list_funcionario')

    @property
    def total_horas_extra(self):
        return self.horaextra_set.all().aggregate(Sum('horas'))['horas__sum']

    def __str__(self):
        return self.nome