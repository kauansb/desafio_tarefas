from django import forms
from .models import RegistroTempo


class RegistroTempoForm(forms.ModelForm):
    class Meta:
        model = RegistroTempo
        fields = ['tarefa', 'horas_trabalhadas', 'descricao']
