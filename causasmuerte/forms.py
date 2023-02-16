from django import forms
from .models import CausaMuerte

class CausaMuerteForm(forms.ModelForm):
    class Meta:
        model = CausaMuerte
        fields = [
            'causa'
        ]

    causa = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'pattern': '[A-Za-z\s]+'}))