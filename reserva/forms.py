from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['recurso','usuario', 'data', 'hora']

        widgets = {
            'recurso': forms.Select(attrs={
                'class': 'form-control',
                'default': 'Escolha um recurso'
            }),
        }