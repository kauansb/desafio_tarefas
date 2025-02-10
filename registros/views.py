from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils.dateparse import parse_date
from django.views.generic import ListView, CreateView

from registros.models import RegistroTempo
from registros.forms import RegistroTempoForm


class ListaRegistrosView(ListView):
    model = RegistroTempo
    template_name = 'registros/lista_registros.html'
    context_object_name = 'registros'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        filtros = Q() # Cria uma única expressão de filtro

        usuario = self.request.GET.get('usuario')
        if usuario:            
            filtros &= Q(tarefa__usuario_responsavel__username=usuario)

        tarefa = self.request.GET.get('tarefa')
        if tarefa:
            filtros &= Q(tarefa__descricao__icontains=tarefa)

        data = self.request.GET.get('data')
        if data:
            data_formatada = parse_date(data)
            filtros &= Q(data_registro__date=data_formatada)

        horas_trabalhadas = self.request.GET.get('horas_trabalhadas')
        if horas_trabalhadas and horas_trabalhadas.isdigit():
            filtros &= Q(horas_trabalhadas=horas_trabalhadas)

        return queryset.filter(filtros) # Aplica todos os filtros de uma vez


class CriarRegistroTempoView(CreateView):
    model = RegistroTempo
    form_class = RegistroTempoForm
    template_name = 'registros/criar_registro.html'
    success_url = reverse_lazy('lista_registros')

    def form_valid(self, form):
        messages.success(self.request, 'Registro de tempo adicionado com sucesso!')
        return super().form_valid(form)
