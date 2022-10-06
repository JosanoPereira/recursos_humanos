from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import Empresa
from django.urls import reverse_lazy

# Create your views here.


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']
    # success_url = reverse_lazy('home')

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('OK')


class EmpresaUpdate(UpdateView):
    model = Empresa
    fields = ['nome']