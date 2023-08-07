import pytest
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_integration(client):
    # Création des objets Address et Letting
    address = Address.objects.create(
        number=123,
        street="Main Street",
        city="CityName",
        state="ST",
        zip_code=12345,
        country_iso_code="USA"
    )
    letting = Letting.objects.create(title="Title Here", address=address)

    # Accès à la page d'index et vérification du code de statut
    response = client.get(reverse('lettings_index'))
    assert response.status_code == 200

    # Vérification que la location créée est présente dans le contenu de la page
    assert b'Title Here' in response.content

    # Accès à la page de détail de la location et vérification du code de statut
    response = client.get(reverse('letting', args=[letting.id]))
    assert response.status_code == 200

    # Vérification que l'adresse est correctement affichée sur la page
    assert b'123 Main Street' in response.content
