from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Funcionario
import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas

from django.template.loader import get_template
import xhtml2pdf.pisa as pisa


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


def pdf_reportlab(request):
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(230, 810, "Relatório dos Funcionários")

    funcionarios = Funcionario.objects.all()

    str_ = 'Nome: %s | Horas: %s | Empresa: %s'
    y = 790
    for funcionario in funcionarios:
        p.drawString(10, y, str_ % (
            funcionario.nome, funcionario.total_horas_extra,
            funcionario.empresa
        ))
        y -= 20

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


class Render:
    @staticmethod
    def render(path: str, params: str, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode('UTF-8')), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse('Erro ao renderizar PDF', status=400)


class PDF(View):
    def get(self, request):
        params = {
            'today': 'variavel today',
            'sales': 'variavel sabes',
            'request': request
        }

        return Render.render('funcionarios/relatorio.html', params, 'myfile')
