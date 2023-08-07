"""
Ce module définit les chemins URL spécifiques aux profils d'utilisateurs. Il inclut un chemin
pour la page d'index des profils et un chemin pour afficher les détails d'un profil
individuel en fonction de son nom d'utilisateur.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="profiles_index"),
    path("<str:username>/", views.profile, name="profile"),
]
