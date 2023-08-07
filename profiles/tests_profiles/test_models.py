"""
Module de tests pour les modèles de l'application "Profiles".
Ces tests vérifient que les représentations sous forme de chaînes de caractères,
des modèles sont correctes.
"""

import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_string_representation():
    """
    Teste la représentation sous forme de chaîne de caractères, du profil.
    Vérifie que le nom d'utilisateur est correctement utilisé
    dans la représentation sous forme de chaîne de caractères du profil.
    """
    user = User.objects.create(username='john_doe')
    profile = Profile(user=user, favorite_city='Paris')
    assert str(profile) == 'john_doe'
