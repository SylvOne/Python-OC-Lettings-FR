"""
Module de tests pour les URL de l'application "Lettings".
Ces tests vérifient que les URL sont résolues correctement.
"""

from django.urls import reverse, resolve
from lettings.views import index, letting


def test_index_url():
    """Teste l'URL de l'index des lettings."""
    url = reverse('lettings_index')
    assert resolve(url).func == index


def test_letting_url():
    """Teste l'URL de détail d'un letting."""
    url = reverse('letting', args=['1'])
    assert resolve(url).func == letting
