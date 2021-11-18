from django.db import models
from characters.models import Character
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Campaign(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    owner=models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True, null=True, max_length = 500)
    characters=models.ManyToManyField(Character, default=None, blank=True, null=True)

    def __str__(self):
        return "%s" %(self.name)

    def get_absolute_url(self):
        return reverse('campaign', kwargs={'campaignpk': self.pk})
