"""
Ce module définit les chemins URL spécifiques aux locations. Il inclut un chemin pour
la page d'index des locations et un chemin pour afficher les détails d'une location
individuelle en fonction de son identifiant.
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='lettings_index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
