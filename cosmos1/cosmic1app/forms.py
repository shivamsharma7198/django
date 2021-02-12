from django import forms
from .models import Cosmos

class CosmicForm(forms.ModelForm):
    class Meta:
        model = Cosmos
        fields = [
            'planetary_body',
            'category',
            'distance',
            'moons',

        ]