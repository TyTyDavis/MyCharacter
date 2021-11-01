
from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('create/', views.createCharacter, name='create'),
    path('edit/<int:pk>', views.characterUpdate.as_view(), name='edit'),
    path('delete/<int:pk>', views.characterDelete.as_view(), name='delete'),
]
