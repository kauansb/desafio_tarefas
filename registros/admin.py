from django.contrib import admin
from registros.models import RegistroTempo


@admin.register(RegistroTempo)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('id','tarefa','data_registro', 'horas_trabalhadas','descricao')
    list_filter = ('data_registro', 'tarefa')
    search_fields = ('tarefa__descricao', 'data_registro', 'horas_trabalhadas', 'descricao')
