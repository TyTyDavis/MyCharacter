from django import forms
from .models import Character


class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        exclude = ['updated_on','created_on']
        widgets = {
            'strength': forms.NumberInput(attrs={'size': 2}),
            'dexterity': forms.NumberInput(attrs={'size': 2}),
        }
