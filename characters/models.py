from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from . import writer


# Create your models here.
class Character(models.Model):
    #add saves
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    #top box
    name = models.CharField(max_length=100)
    characterClass = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    level = models.IntegerField(default=1,validators=[MaxValueValidator(20), MinValueValidator(1)])
    background = models.CharField(max_length=100)
    alignment = models.CharField(max_length=2)
    playerName = models.CharField(max_length=20, blank=True, null=True)

    experiencePoints = models.IntegerField(blank=True, null=True,validators=[MaxValueValidator(355000), MinValueValidator(1)])
    inspiration = models.IntegerField(blank=True, null=True,validators=[MaxValueValidator(99), MinValueValidator(1)])
    armorClass = models.IntegerField(default=10,validators=[MaxValueValidator(50), MinValueValidator(1)])
    speed = models.IntegerField(default=30,validators=[MaxValueValidator(99), MinValueValidator(1)])
    hitDie = models.CharField(max_length=4, blank=True, null=True)
    hitDieTotal = models.IntegerField(default=1,validators=[MaxValueValidator(20), MinValueValidator(1)])
    proficiency = models.IntegerField(default=1,validators=[MaxValueValidator(20), MinValueValidator(1)])
    hp = models.IntegerField(default=1,validators=[MaxValueValidator(200), MinValueValidator(1)])
    #saves
    strengthSave = models.BooleanField(default=False)
    dexteritySave = models.BooleanField(default=False)
    constitutionSave = models.BooleanField(default=False)
    intelligenceSave = models.BooleanField(default=False)
    wisdomSave = models.BooleanField(default=False)
    charismaSave = models.BooleanField(default=False)
    #abilities
    strength = models.IntegerField(default=10,validators=[MaxValueValidator(35), MinValueValidator(1)])
    dexterity = models.IntegerField(default=10,validators=[MaxValueValidator(35), MinValueValidator(1)])
    constitution = models.IntegerField(default=10,validators=[MaxValueValidator(35), MinValueValidator(1)])
    intelligence = models.IntegerField(default=10,validators=[MaxValueValidator(35), MinValueValidator(1)])
    wisdom = models.IntegerField(default=10,validators=[MaxValueValidator(35), MinValueValidator(1)])
    charisma = models.IntegerField(default=10,validators=[MaxValueValidator(35), MinValueValidator(1)])


    #skills
    acrobatics = models.IntegerField(default=0, blank=True, null=True)
    acrobaticsProficiency = models.BooleanField(default=False)
    animalHandling = models.IntegerField(default=0,blank=True, null=True)
    animalHandlingProficiency = models.BooleanField(default=False)
    arcana = models.IntegerField(default=0,blank=True, null=True)
    arcanaProficiency = models.BooleanField(default=False)
    athletics = models.IntegerField(default=0,blank=True, null=True)
    athleticsProficiency = models.BooleanField(default=False)
    deception = models.IntegerField(default=0,blank=True, null=True)
    deceptionProficiency = models.BooleanField(default=False)
    history = models.IntegerField(default=0,blank=True, null=True)
    historyProficiency = models.BooleanField(default=False)
    insight = models.IntegerField(default=0,blank=True, null=True)
    insightProficiency = models.BooleanField(default=False)
    intimidation = models.IntegerField(default=0,blank=True, null=True)
    intimidationProficiency = models.BooleanField(default=False)
    investigation = models.IntegerField(default=0,blank=True, null=True)
    investigationProficiency = models.BooleanField(default=False)
    medicine = models.IntegerField(default=0,blank=True, null=True)
    medicineProficiency = models.BooleanField(default=False)
    nature = models.IntegerField(default=0,blank=True, null=True)
    natureProficiency = models.BooleanField(default=False)
    perception = models.IntegerField(default=0,blank=True, null=True)
    perceptionProficiency = models.BooleanField(default=False)
    performance = models.IntegerField(default=0,blank=True, null=True)
    performanceProficiency = models.BooleanField(default=False)
    persuasion = models.IntegerField(default=0,blank=True, null=True)
    persuasionProficiency = models.BooleanField(default=False)
    religion = models.IntegerField(default=0,blank=True, null=True)
    religionProficiency = models.BooleanField(default=False)
    sleightOfHand = models.IntegerField(default=0,blank=True, null=True)
    sleightOfHandProficiency = models.BooleanField(default=False)
    stealth = models.IntegerField(default=0,blank=True, null=True)
    stealthProficiency = models.BooleanField(default=False)
    survival = models.IntegerField(default=0,blank=True, null=True)
    survivalProficiency = models.BooleanField(default=False)

    #combat
    weapon1Name = models.CharField(blank=True, null=True, max_length=100)
    weapon1Attack = models.IntegerField(blank=True, null=True, default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    weapon1Dmg = models.CharField(blank=True, null=True, max_length=20)
    weapon2Name = models.CharField(blank=True, null=True, max_length=100)
    weapon2Attack = models.IntegerField(blank=True, null=True, default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    weapon2Dmg = models.CharField(blank=True, null=True, max_length=20)

    #spells
    spells = models.TextField(blank=True, null=True, max_length = 500)

    #equipment
    equipment = models.TextField(default="", max_length = 500)
    cp = models.IntegerField(default=0,validators=[MaxValueValidator(999), MinValueValidator(0)])
    sp = models.IntegerField(default=0,validators=[MaxValueValidator(999), MinValueValidator(0)])
    ep = models.IntegerField(default=0,validators=[MaxValueValidator(999), MinValueValidator(0)])
    gp = models.IntegerField(default=0,validators=[MaxValueValidator(999), MinValueValidator(0)])
    pp = models.IntegerField(default=0,validators=[MaxValueValidator(999), MinValueValidator(0)])

    #languages and proficiencies
    languages = models.TextField(blank=True, null=True, max_length = 500)
    proficiencies = models.TextField(blank=True, null=True, max_length = 500)

    traits = models.TextField(blank=True, null=True,max_length = 1000)

    #flavor
    personality = models.TextField(blank=True, null=True,max_length = 500)
    ideals = models.TextField(blank=True, null=True,max_length = 500)
    bonds = models.TextField(blank=True, null=True,max_length = 500)
    flaws = models.TextField(blank=True, null=True,max_length = 500)

    strBonus = models.IntegerField(blank=True, null=True)
    dexBonus = models.IntegerField(blank=True, null=True)
    conBonus = models.IntegerField(blank=True, null=True)
    intBonus = models.IntegerField(blank=True, null=True)
    wisBonus = models.IntegerField(blank=True, null=True)
    chaBonus = models.IntegerField(blank=True, null=True)

    passivePerception = models.IntegerField(default=0, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.strBonus = writer.abilityBonus(self.strength)
        self.dexBonus = writer.abilityBonus(self.dexterity)
        self.conBonus = writer.abilityBonus(self.constitution)
        self.intBonus = writer.abilityBonus(self.intelligence)
        self.wisBonus = writer.abilityBonus(self.wisdom)
        self.chaBonus = writer.abilityBonus(self.charisma)

        self.acrobatics = self.dexBonus + writer.skillProficient(self, self.acrobaticsProficiency)
        self.animalHandling = self.wisBonus + writer.skillProficient(self, self.animalHandlingProficiency)
        self.arcana = self.intBonus + writer.skillProficient(self, self.arcanaProficiency)
        self.athletics = self.strBonus + writer.skillProficient(self, self.athleticsProficiency)
        self.deception = self.chaBonus + writer.skillProficient(self, self.deceptionProficiency)
        self.history = self.intBonus + writer.skillProficient(self, self.historyProficiency)
        self.insight = self.wisBonus + writer.skillProficient(self, self.insightProficiency)
        self.intimidation = self.chaBonus + writer.skillProficient(self, self.intimidationProficiency)
        self.investigation = self.intBonus + writer.skillProficient(self, self.investigationProficiency)
        self.medicine = self.wisBonus + writer.skillProficient(self, self.medicineProficiency)
        self.nature = self.intBonus + writer.skillProficient(self, self.natureProficiency)
        self.perception = self.wisBonus + writer.skillProficient(self, self.perceptionProficiency)
        self.performance = self.chaBonus + writer.skillProficient(self, self.performanceProficiency)
        self.persuasion = self.chaBonus + writer.skillProficient(self, self.persuasionProficiency)
        self.religion = self.intBonus + writer.skillProficient(self, self.religionProficiency)
        self.sleightOfHand = self.dexBonus + writer.skillProficient(self, self.sleightOfHandProficiency)
        self.stealth = self.dexBonus + writer.skillProficient(self, self.stealthProficiency)
        self.survival = self.wisBonus + writer.skillProficient(self, self.survivalProficiency)


        self.passivePerception = self.perception + 10

        super(Character, self).save(*args, **kwargs) # Call the "real" save() method.

    def __str__(self):
        return "%s, %s %s" %(self.name, self.race, self.characterClass)

    def get_absolute_url(self):
        return reverse('character', kwargs={'char_pk': self.pk})


    def has_change_permission(self, request, obj=None):
        if obj is not None:
            if request.user.is_superuser:
                return True
            else:
                if obj.user != request.user:
                    return False
                else:
                    return True
