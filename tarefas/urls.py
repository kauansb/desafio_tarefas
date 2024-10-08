from django.urls import path
from .views import CriarTarefaView, ListaTarefasView


urlpatterns = [
    path('', ListaTarefasView.as_view(), name='lista_tarefas'),
    path('nova/', CriarTarefaView.as_view(), name='criar_tarefa'),
]
