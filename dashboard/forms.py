from django import forms
from .models import Trader

class TraderForm(forms.ModelForm):
    class Meta:
        model = Trader
        fields = ['name', 'initial_balance', 'current_balance']
