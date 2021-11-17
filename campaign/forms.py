from django import forms
from characters.models import Character
from campaign.models import Character


class addCharacterForm(forms.Form):
    characterpk = forms.IntegerField()
