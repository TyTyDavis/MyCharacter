from django.shortcuts import render
from django.http import HttpResponse
from characters.models import Character
from django.urls import reverse_lazy
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def home(request):
    return render(request, "main/home.html", {})


def characterView(request, char_pk):

    a = get_object_or_404(Character, pk=char_pk)
    return render(request,"character.html",{"name" : a.name, "characterClass" : a.characterClass, "race" : a.race, "pk" : a.pk })

class characterCreate(CreateView):
    model = Character
    fields = "__all__"

class characterUpdate(UpdateView):
    model = Character
    fields = "__all__"
    template_name_suffix = '_update_form'

class characterDelete(DeleteView):
    model = Character
    success_url = reverse_lazy('home')
    template_name_suffix = '_check_delete'
