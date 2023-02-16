from django import forms
from .models import Nacionalidad

class NacionalidadForm(forms.ModelForm):
    class Meta:
        model = Nacionalidad
        fields = [
            'nacionalidad'
        ]

    nacionalidad = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'pattern': '[A-Za-z\s]+'}))