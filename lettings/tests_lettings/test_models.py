"""
Module de tests pour les modèles de l'application "Lettings".
Ces tests vérifient que les représentations sous forme de chaînes de caractères,
des modèles sont correctes.
"""

import pytest
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_string_representation():
    """
    Teste la représentation sous forme de chaîne de caractères, de l'adresse.
    """
    address = Address(
        number=123,
        street="Main Street",
        city="CityName",
        state="ST",
        zip_code=12345,
        country_iso_code="USA"
    )
    assert str(address) == '123 Main Street'


@pytest.mark.django_db
def test_letting_string_representation():
    """
    Teste la représentation sous forme de chaîne de caractères, du letting.
    """
    address = Address.objects.create(
        number=123,
        street="Main Street",
        city="CityName",
        state="ST",
        zip_code=12345,
        country_iso_code="USA"
    )
    letting = Letting(title="Title Here", address=address)
    assert str(letting) == 'Title Here'
