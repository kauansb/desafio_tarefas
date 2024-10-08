from django.views.generic import ListView
from registros.models import RegistroTempo


class ListaRegistrosView(ListView):
    model = RegistroTempo
    template_name = 'registros/lista_registros.html'
    context_object_name = 'registros'
