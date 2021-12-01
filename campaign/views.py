from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.contrib.staticfiles.storage import staticfiles_storage
from django.templatetags.static import static
from campaign.models import Campaign
from characters.models import Character
from .forms import addCharacterForm

# Create your views here.
class campaignCreate(CreateView):
    model = Campaign
    fields=['name', 'description', 'characters']

    def form_valid(self, form):
        campaign = form.save(commit=False)
        campaign.owner = self.request.user
        campaign.save()

        return super(campaignCreate, self).form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("form invalid")
        print('error')
        print(form.errors, len(form.errors))

class campaignUpdate(UpdateView):
    model = Campaign
    fields=['name', 'description']
    def form_valid(self, form):
        campaign = form.save(commit=False)
        if campaign.owner == self.request.user:
            campaign.save()
            return super(campaignCreate, self).form_valid(form)
        else:
            return redirect('home')

class campaignDelete(DeleteView):
    model = Campaign
    success_url = reverse_lazy('home')
    template_name_suffix = '_check_delete'

class campaignView(TemplateView):
    template_name = "campaign.html"
    formClass = addCharacterForm
    #success_url = ''


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = addCharacterForm(self.request.POST or None)
        context['form'] = form
        context['campaignpk']=self.kwargs['campaignpk']
        context['campaign'] = get_object_or_404(Campaign, pk=context['campaignpk'])
        context['characters'] = context['campaign'].characters.all()
        return context




    def post(self, request, *args, **kwargs):
        # check whether it's valid:
        context = self.get_context_data()

        if context["form"].is_valid():
            if not Character.objects.filter(pk=self.request.POST.get('characterpk')).exists():
                context['not_valid'] = True
                return render(request, 'campaign.html', context)
            else:
                characterObj = get_object_or_404(Character, pk=self.request.POST.get('characterpk'))
                context['campaign'].characters.add(characterObj)
                return render(request, 'campaign.html', context)

        else:
            context['not_valid'] = True
            return render(request, 'campaign.html', context)


class campaignList(ListView):
    model = Campaign
    template_name = "campaignList.html"
    context_object_name = "campaigns"

    def get_queryset(self):
         return Campaign.objects.filter(owner = self.request.user).order_by('-updated_on')

def removeCharacterFromCampaign(request, campaignpk, characterpk):
    #change this to post
    if request.method =="GET":
        campaignObj = get_object_or_404(Campaign, pk=campaignpk)
        characterObj = get_object_or_404(Character, pk=characterpk)
        return render(request, "campaign/campaign_remove.html", context={'campaign': campaignObj, 'character': characterObj })
    elif request.method == "POST":
        campaignObj = get_object_or_404(Campaign, pk=campaignpk)
        characterObj = get_object_or_404(Character, pk=characterpk)
        campaignObj.characters.remove(characterObj)
        return redirect('campaign', campaignpk=campaignpk)
