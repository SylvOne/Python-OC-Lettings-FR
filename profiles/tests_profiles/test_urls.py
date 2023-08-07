"""
Module de tests pour les chemins d'URL de l'application "Profiles".
Ces tests vérifient que les URL sont résolues correctement.
"""

from django.urls import reverse, resolve
from profiles.views import index, profile


def test_index_url():
    """
    Teste l'URL de la page d'index des profils.
    Vérifie que l'URL résout correctement la fonction de vue 'index'.
    """
    url = reverse('profiles_index')
    assert resolve(url).func == index


def test_profile_url():
    """
    Teste l'URL de la page de profil individuelle.
    Vérifie que l'URL résout correctement la fonction de vue 'profile'
    pour un nom d'utilisateur donné.
    """
    url = reverse('profile', args=['john_doe'])
    assert resolve(url).func == profile
