from django.shortcuts import render
from django.http import HttpResponse
from characters.models import Character
from django.urls import reverse_lazy
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
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
    form_class = CharacterForm

    def form_valid(self, form):
        character = form.save(commit=False)
        character.author = self.request.user
        character.save()

        return super(characterCreate, self).form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("form invalid")
        print('error')
        print(form.errors, len(form.errors))

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
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home')
        else:
            print('error')
            print(form.errors, len(form.errors))
    else:
        form = CharacterForm()
    return render(request, 'characters/character_form.html', {'form': form})


def characterSheetView(request, pk):
    character = Character.objects.get(pk=pk)

    sheet = Image.open(staticfiles_storage.path('blankSheet.png'))
    sheet_io = BytesIO()
    writer.writeSheet(sheet, character)
    sheet.save(sheet_io, format='PNG')
    sheet_file = InMemoryUploadedFile(sheet_io, None, 'foo.jpg', 'jpeg', None, None)
    return HttpResponse(sheet_file, content_type="image/png")


class characterView(TemplateView):
    template_name = "character.html"
    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['character'] = get_object_or_404(Character, pk=context['char_pk'])
        return context

class characterList(ListView):
    model = Character
    template_name = "characterList.html"
    context_object_name = "characters"

    def get_queryset(self):
         return Character.objects.filter(author = self.request.user).order_by('-updated_on')
