from django.shortcuts import render
from django.http import HttpResponse
from characters.models import Character
from django.urls import reverse_lazy
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView, View
from .forms import CharacterForm
from django.shortcuts import redirect
from django.contrib.staticfiles.storage import staticfiles_storage
from django.templatetags.static import static
from PIL import Image
from django.core.files.temp import NamedTemporaryFile
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from . import writer

# Create your views here.


def home(request):
    return render(request, "main/home.html", {})

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

def createCharacter(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)

        if form.is_valid():
            return redirect('home')
    else:
        form = CharacterForm()
    return render(request, 'characters/character_form.html', {'form': form})

#def characterView(request, char_pk):
#    char = get_object_or_404(Character, pk=char_pk)
#    imagePath = fontFile = staticfiles_storage.path('blankSheet.png')
#    img = Image.open(imagePath)
#    writer.writeSheet(img, char)
#    return render(request,"character.html",{"name" : char.name, "characterClass" : char.characterClass, "race" : char.race, "pk" : char.pk })


def characterSheetView(request, pk):
    #CONVERT FROM pil IMAGE TO DJANGO FILE
    # Create a file-like object to write thumb data (thumb data previously created
    # using PIL, and stored in variable 'thumb')
    character = Character.objects.get(pk=pk)

    sheet = Image.open(staticfiles_storage.path('blankSheet.png'))
    sheet_io = BytesIO()
    writer.writeSheet(sheet, character)
    sheet.save(sheet_io, format='PNG')

    # Create a new Django file-like object to be used in models as ImageField using
    # InMemoryUploadedFile.  If you look at the source in Django, a
    # SimpleUploadedFile is essentially instantiated similarly to what is shown here
    sheet_file = InMemoryUploadedFile(sheet_io, None, 'foo.jpg', 'jpeg', None, None)

    #sheet_temp = NamedTemporaryFile()

    #writeSheet(sheet, char_pk)
    #sheet.save(sheet_temp)
    #image_data = open(staticfiles_storage.path('blankSheet.png'), encoding="utf8").read()
    return HttpResponse(sheet_file, content_type="image/png")
    #sheet_temp.close()


class characterView(TemplateView):
    template_name = "character.html"
    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['character'] = get_object_or_404(Character, pk=context['char_pk'])
        return context
