from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Character(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    #top box
    name = models.CharField(max_length=100)
    characterClass = models.CharField(max_length=100)
    race= models.CharField(max_length=100)
    level = models.IntegerField(default=1,validators=[MaxValueValidator(20), MinValueValidator(1)])
    background = models.CharField(max_length=100)
    alignment = models.CharField(max_length=2)
    playerName = models.CharField(max_length=100)

    experiencePoints = models.IntegerField(blank=True, null=True,validators=[MaxValueValidator(355000), MinValueValidator(1)])
    inspiration = models.IntegerField(blank=True, null=True,validators=[MaxValueValidator(99), MinValueValidator(1)])
    armorClass = models.IntegerField(default=10,validators=[MaxValueValidator(50), MinValueValidator(1)])
    speed = models.IntegerField(default=30,validators=[MaxValueValidator(99), MinValueValidator(1)])
    hitDie = models.CharField(max_length=4)
    hitDieTotal = models.IntegerField(default=1,validators=[MaxValueValidator(20), MinValueValidator(1)])
    proficiency = models.IntegerField(default=1,validators=[MaxValueValidator(20), MinValueValidator(1)])

    #abilities
    strength = models.IntegerField(default=10,validators=[MaxValueValidator(35), MinValueValidator(1)])
    dexterity = models.IntegerField(default=10,validators=[MaxValueValidator(35), MinValueValidator(1)])
    constitution = models.IntegerField(default=10,validators=[MaxValueValidator(35), MinValueValidator(1)])
    intelligence = models.IntegerField(default=10,validators=[MaxValueValidator(35), MinValueValidator(1)])
    wisdom = models.IntegerField(default=10,validators=[MaxValueValidator(35), MinValueValidator(1)])
    charisma = models.IntegerField(default=10,validators=[MaxValueValidator(35), MinValueValidator(1)])

    #skills
    acrobatics = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    acrobaticsProficiency = models.BooleanField(default=False)
    animalHandling = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    animalHandlingProficiency = models.BooleanField(default=False)
    arcana = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    arcanaProficiency = models.BooleanField(default=False)
    athletics = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    athleticsProficiency = models.BooleanField(default=False)
    deception = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    deceptionProficiency = models.BooleanField(default=False)
    history = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    historyProficiency = models.BooleanField(default=False)
    insight = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    insightProficiency = models.BooleanField(default=False)
    intimidation = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    intimidationProficiency = models.BooleanField(default=False)
    investigation = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    investigationProficiency = models.BooleanField(default=False)
    medicine = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    medicineProficiency = models.BooleanField(default=False)
    nature = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    natureProficiency = models.BooleanField(default=False)
    perception = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    perceptionProficiency = models.BooleanField(default=False)
    performance = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    performanceProficiency = models.BooleanField(default=False)
    religion = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    religionProficiency = models.BooleanField(default=False)
    sleightOfHand = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    sleightOfHandProficiency = models.BooleanField(default=False)
    stealth = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    stealthProficiency = models.BooleanField(default=False)
    survival = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    survivalProficiency = models.BooleanField(default=False)

    #combat
    weapon1Name = models.CharField(max_length=100)
    weapon1Attack = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    weapon1Dmg = models.CharField(max_length=20)
    weapon2Name = models.CharField(max_length=100)
    weapon2Attack = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(-20)])
    weapon2Dmg = models.CharField(max_length=20)

    #spells
    spells = models.TextField(max_length = 500)

    #equipment
    equipment = models.TextField(max_length = 500)
    cp = models.IntegerField(default=0,validators=[MaxValueValidator(999), MinValueValidator(0)])
    sp = models.IntegerField(default=0,validators=[MaxValueValidator(999), MinValueValidator(0)])
    ep = models.IntegerField(default=0,validators=[MaxValueValidator(999), MinValueValidator(0)])
    gp = models.IntegerField(default=0,validators=[MaxValueValidator(999), MinValueValidator(0)])
    pp = models.IntegerField(default=0,validators=[MaxValueValidator(999), MinValueValidator(0)])

    #languages and proficiencies
    languages = models.TextField(max_length = 500)
    proficiencies = models.TextField(max_length = 500)

    traits = models.TextField(max_length = 1000)

    #flavor
    personality = models.TextField(max_length = 500)
    ideals = models.TextField(max_length = 500)
    bonds = models.TextField(max_length = 500)
    flaws = models.TextField(max_length = 500)


    def __str__(self):
        return "%s, %s %s" %(self.name, self.race, self.characterClass)

    def get_absolute_url(self):
        return reverse('character', kwargs={'char_pk': self.pk})
