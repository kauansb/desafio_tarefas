from django.db import models
from django.contrib.auth.models import User


class Tarefa(models.Model):
    usuario_responsavel = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas')
    data_criacao = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.usuario_responsavel} - {self.descricao[:20]}"