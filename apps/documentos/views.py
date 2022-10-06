from django.shortcuts import render
from django.views.generic import (ListView, CreateView,
                                  DeleteView, UpdateView)
from .models import Documento
from django.urls import reverse_lazy


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['num_doc', 'arquivo']
    success_url = reverse_lazy('list_funcionario')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.dono_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['btn'] = 'Cadastrar documento'
        return context




