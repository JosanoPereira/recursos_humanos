from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Funcionario


class FuncionarioList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_on = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_on)


class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    success_url = reverse_lazy('list_funcionario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['btn'] = 'Atualizar'
        return context


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionario')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['btn'] = 'Criar'
        return context

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)