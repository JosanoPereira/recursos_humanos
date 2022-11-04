import csv
import json
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
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
    # success_url = reverse_lazy('list_hora_extra')

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
        kwargs = super(HoraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['btn'] = 'Criar hora'
        return context


class UtitizouHoraExtra(View):
    def post(self, *args, **kwargs):
        # HoraExtra.objects.last().save()
        registro_hora_extra = HoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()

        empregado = self.request.user.funcionario
        response = json.dumps(
            {'mensagem': 'Requisição executada!',
             'horas': float(empregado.total_horas_extra)}
        )

        return HttpResponse(response, content_type='application/json')


class RelatorioCSV(View):
    def get(self, request):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="teste.csv"'
        horas_extras = HoraExtra.objects.filter(utilizada=False)
        writer = csv.writer(response)
        writer.writerow(['ID', 'Motivo', 'Funcionário', 'Horas', 'Total de Horas'])
        for horas in horas_extras:
            writer.writerow([
                horas.id, horas.motivo, horas.funcionario, horas.horas, horas.funcionario.total_horas_extra
            ])

        return response