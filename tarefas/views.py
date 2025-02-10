from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from tarefas.models import Tarefa
from tarefas.forms import TarefaModelForm


class ListaTarefasView(ListView):
    model = Tarefa
    template_name = 'tarefas/lista_tarefas.html'
    context_object_name = 'tarefas'
    paginate_by = 10


class CriarTarefaView(CreateView):
    model = Tarefa
    form_class = TarefaModelForm
    template_name = 'tarefas/criar_tarefa.html'
    success_url = reverse_lazy('lista_tarefas')

    def form_valid(self, form):
        messages.success(self.request, 'Tarefa criada com sucesso!')
        return super().form_valid(form)