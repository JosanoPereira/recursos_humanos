from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import HoraExtraForm
from .models import HoraExtra

# Create your views here.


class HoraList(ListView):
    model = HoraExtra

    def get_queryset(self):
        empresa_on = self.request.user.funcionario.empresa
        return HoraExtra.objects.filter(funcionario__empresa=empresa_on)


class HoraUpdate(UpdateView):
    model = HoraExtra
    # fields = ['motivo', 'horas', 'funcionario']
    form_class = HoraExtraForm
    success_url = reverse_lazy('list_hora_extra')

    def get_form_kwargs(self):
        kwargs = super(HoraUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['btn'] = 'Atualizar hora'
        return context


class HoraDelete(DeleteView):
    model = HoraExtra
    success_url = reverse_lazy('list_hora_extra')


class HoraCreate(CreateView):
    model = HoraExtra
    # fields = ['motivo', 'horas', 'funcionario']
    form_class = HoraExtraForm
    success_url = reverse_lazy('list_hora_extra')

    def get_form_kwargs(self):
        kwargs =  super(HoraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['btn'] = 'Criar hora'
        return context