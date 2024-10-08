from django.contrib import admin
from django.urls import path

from registros.views import ListaRegistrosView
from tarefas.views import ListaTarefasView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('tarefas/', ListaTarefasView.as_view(), name='lista_tarefas'),
    path('registros/', ListaRegistrosView.as_view(), name='lista_registros'),]
