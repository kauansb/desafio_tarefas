from django import forms
from tarefas.models import Tarefa


class TarefaModelForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['usuario_responsavel', 'descricao']