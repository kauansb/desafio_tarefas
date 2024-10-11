from django.db import models
from tarefas.models import Tarefa


class RegistroTempo(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE, related_name='registros_de_tempo')
    data_registro = models.DateTimeField(auto_now_add=True)
    horas_trabalhadas = models.IntegerField()
    descricao = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.tarefa} - {self.horas_trabalhadas} horas"