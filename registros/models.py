from django.db import models
from tarefas.models import Tarefa


class RegistroTempo(models.Model):
    tarefa = models.ForeignKey(Tarefa,on_delete=models.CASCADE, related_name='registros_de_tempo')
    data_registro = models.DateTimeField(auto_now_add=True)
    horas_trabalhadas = models.DecimalField(max_digits=4, decimal_places=1)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.tarefa} - {self.horas_trabalhadas} horas"