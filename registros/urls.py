from django.urls import path
from .views import CriarRegistroTempoView, ListaRegistrosView


urlpatterns = [
    path('', ListaRegistrosView.as_view(), name='lista_registros'),
    path('novo/', CriarRegistroTempoView.as_view(), name='criar_registro'),
]
