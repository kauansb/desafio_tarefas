from django.contrib import admin
from tarefas.models import Tarefa


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('id','usuario_responsavel','data_criacao','descricao')
    search_fields = ('usuario_responsavel__username', 'data_criacao', 'descricao',)