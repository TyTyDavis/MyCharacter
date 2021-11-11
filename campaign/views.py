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

# Create your views here.
class campaignCreate(CreateView):
    model = Campaign
    fields=['name', 'description']

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

class campaignDelete(DeleteView):
    model = Campaign
    success_url = reverse_lazy('home')
    template_name_suffix = '_check_delete'

class campaignView(TemplateView):
    template_name = "campaign.html"
    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = get_object_or_404(Campaign, pk=context['pk'])
        return context

class campaignList(ListView):
    model = Campaign
    template_name = "campaignList.html"
    context_object_name = "campaigns"

    def get_queryset(self):
         return Campaign.objects.filter(owner = self.request.user).order_by('-updated_on')
