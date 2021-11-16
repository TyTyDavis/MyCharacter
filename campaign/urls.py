from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('create/', views.campaignCreate.as_view(), name='createCampaign'),
    path('campaignlist/', views.campaignList.as_view(), name='campaignList'),
    path('edit/<int:pk>', views.campaignUpdate.as_view(), name='campaignEdit'),
    path('delete/<int:pk>', views.campaignDelete.as_view(), name='campaignDelete'),
    path('<int:pk>/', views.campaignView.as_view(), name='campaign'),
    path('remove/<int:campaignpk>/<int:characterpk>', views.removeCharacterFromCampaign, name='remove'),
]
