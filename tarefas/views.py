from django.views.generic import ListView
from tarefas.models import Tarefa


class ListaTarefasView(ListView):
    model = Tarefa
    template_name = 'tarefas/lista_tarefas.html'
    context_object_name = 'tarefas'