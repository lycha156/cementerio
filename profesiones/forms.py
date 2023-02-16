from django import forms
from .models import Profesion

class ProfesionForm(forms.ModelForm):
    class Meta:
        model = Profesion
        fields = [
            'profesion'
        ]

    profesion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'pattern': '[A-Za-z\s]+'}))