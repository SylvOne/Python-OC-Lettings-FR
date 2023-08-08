"""
Module de tests pour les vues de l'application "Lettings".
Ces tests vérifient les réponses des vues, y compris les codes de statut HTTP.
"""

import pytest
from django.urls import reverse
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_index_view(client):
    """Teste la vue de l'index des lettings."""
    response = client.get(reverse('lettings_index'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_view(client):
    """Teste la vue de détail d'un letting."""
    address = Address.objects.create(
        number=123,
        street="Main Street",
        city="CityName",
        state="ST",
        zip_code=12345,
        country_iso_code="USA"
    )
    letting = Letting.objects.create(title="Title Here", address=address)
    response = client.get(reverse('letting', args=[letting.id]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_view_not_found(client):
    """Teste la vue pour le détail d'un letting pour un ID non existant."""
    non_existent_letting_id = 999999  # cet ID n'existe pas dans la bdd.
    response = client.get(reverse('letting', args=[non_existent_letting_id]))
    assert response.status_code == 404
