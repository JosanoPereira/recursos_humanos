from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Departamento


class DepartamentoList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_on = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_on)


class DepartamentoUpdate(UpdateView):
    model = Departamento
    fields = ['nome']
    success_url = reverse_lazy('list_departamento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['btn'] = 'Atualizar Departamento'
        context['titulo'] = 'Atualizar Departamento'
        return context


class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['btn'] = 'Apagar Departamento'
        context['titulo'] = 'Apagar Departamento'
        return context


class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']
    success_url = reverse_lazy('list_departamento')

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreate, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['btn'] = 'Criar Departamento'
        context['titulo'] = 'Criar Departamento'
        return context