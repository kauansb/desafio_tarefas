from django import forms
from tarefas.models import Tarefa


class TarefaModelForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        filds = ['usuario_responsavel', 'descricao']