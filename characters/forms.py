from django import forms
from .models import Character


class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        exclude = ['updated_on','created_on', 'author']
        widgets = {
            'level': forms.NumberInput(attrs={'style': 'width: 100px'}),
            'characterClass': forms.TextInput(attrs={'style': 'width: 200px'}),
            'alignment': forms.TextInput(attrs={'style': 'width: 100px'}),

            'strength': forms.NumberInput(attrs={'style': 'width: 100px'}),
            'dexterity': forms.NumberInput(attrs={'style': 'width: 100px'}),
            'constitution': forms.NumberInput(attrs={'style': 'width: 100px'}),
            'intelligence': forms.NumberInput(attrs={'style': 'width: 100px'}),
            'wisdom': forms.NumberInput(attrs={'style': 'width: 100px'}),
            'charisma': forms.NumberInput(attrs={'style': 'width: 100px'}),

            'inspiration': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'proficiency': forms.NumberInput(attrs={'style': 'width: 50px'}),

            'acrobatics': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'animalHandling': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'arcana': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'athletics': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'deception': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'history': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'insight': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'intimidation': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'investigation': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'medicine': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'nature': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'perception': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'performance': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'persuasion': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'religion': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'sleightOfHand': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'stealth': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'survival': forms.NumberInput(attrs={'style': 'width: 50px'}),

            'cp': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'sp': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'ep': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'gp': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'pp': forms.NumberInput(attrs={'style': 'width: 50px'}),

            'armorClass': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'speed': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'hitDieTotal': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'hitDie': forms.TextInput(attrs={'style': 'width: 100px'}),
            'hp': forms.TextInput(attrs={'style': 'width: 100px'}),

            'weapon1Name' : forms.TextInput(attrs={'style': 'max-width: 80%'}),
            'weapon2Name' : forms.TextInput(attrs={'style': 'max-width: 80%'}),
            'weapon1Dmg' : forms.TextInput(attrs={'style': 'max-width: 80%'}),
            'weapon2Dmg' : forms.TextInput(attrs={'style': 'max-width: 80%'}),

            'weapon1Attack': forms.NumberInput(attrs={'style': 'width: 50px'}),
            'weapon2Attack': forms.NumberInput(attrs={'style': 'width: 50px'}),

            'languages' : forms.Textarea(attrs={'style': 'max-width: 80%'}),
            'proficiencies' : forms.Textarea(attrs={'style': 'max-width: 80%'}),
            'equipment' : forms.Textarea(attrs={'style': 'max-width: 80%; height: 200px'}),
            'spells' : forms.Textarea(attrs={'style': 'max-width: 80%; height: 200px'}),
            'personality' : forms.Textarea(attrs={'style': 'max-width: 80%; height: 200px'}),
            'ideals' : forms.Textarea(attrs={'style': 'max-width: 80%; height: 200px'}),
            'bonds' : forms.Textarea(attrs={'style': 'max-width: 80%; height: 200px'}),
            'flaws' : forms.Textarea(attrs={'style': 'max-width: 80%; height: 200px'}),
            'traits' : forms.Textarea(attrs={'style': 'max-width: 80%'}),








        }
