from django.contrib.auth.models import User
from django.utils.dateparse import parse_date
from django.db.models import Q
from django.views.generic import ListView
from registros.models import RegistroTempo

class ListaRegistrosView(ListView):
    model = RegistroTempo
    template_name = 'registros/lista_registros.html'
    context_object_name = 'registros'

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtros aplicados via query parameters
        usuario = self.request.GET.get('usuario')
        if usuario:
            try:
                usuario_obj = User.objects.get(username=usuario)
                queryset = queryset.filter(tarefa__usuario_responsavel=usuario_obj)
            except User.DoesNotExist:
                queryset = queryset.none()  # Retorna um queryset vazio se o usuário não for encontrado

        tarefa = self.request.GET.get('tarefa')
        if tarefa:
            queryset = queryset.filter(tarefa__descricao__icontains=tarefa)

        data = self.request.GET.get('data')
        if data:
            data_formatada = parse_date(data)  # Tenta converter a string em uma data válida
            if data_formatada:
                queryset = queryset.filter(data_registro__date=data_formatada)

        horas_trabalhadas = self.request.GET.get('horas_trabalhadas')
        if horas_trabalhadas:
            try:
                queryset = queryset.filter(horas_trabalhadas=horas_trabalhadas)
            except ValueError:
                pass  # Se não for possível converter para float, ignora o filtro

        return queryset
