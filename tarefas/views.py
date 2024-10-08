from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from tarefas.models import Tarefa


class ListaTarefasView(ListView):
    model = Tarefa
    template_name = 'tarefas/lista_tarefas.html'
    context_object_name = 'tarefas'


class CriarTarefaView(CreateView):
    model = Tarefa
    fields = ['usuario_responsavel', 'descricao']
    template_name = 'tarefas/criar_tarefa.html'
    success_url = reverse_lazy('lista_tarefas')