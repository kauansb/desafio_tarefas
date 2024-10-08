from django.contrib import admin
from django.urls import path

from registros.views import CriarRegistroTempoView, ListaRegistrosView
from tarefas.views import CriarTarefaView, ListaTarefasView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('tarefas/', ListaTarefasView.as_view(), name='lista_tarefas'),
    path('nova_tarefa/', CriarTarefaView.as_view(), name='criar_tarefa'),
    
    path('registros/', ListaRegistrosView.as_view(), name='lista_registros'),
    path('novo_registro/', CriarRegistroTempoView.as_view(), name='criar_registro'),
    
    ]
