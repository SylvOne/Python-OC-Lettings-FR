"""
Module de tests d'intégration pour l'application "Profiles".
Ce test vérifie que les modèles, vues, et URLs fonctionnent bien ensemble.
"""

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_user_profile_integration(client):
    """
    Teste l'intégration des composants de l'application "Profiles".
    Vérifie que les utilisateurs et les profils peuvent être créés,
    et que les vues affichent les informations correctes.
    """
    # Créer un utilisateur et un profil
    user = User.objects.create(username='john_doe')
    Profile.objects.create(user=user, favorite_city='Paris')

    # Vérifier que la vue index contient le nom d'utilisateur
    response = client.get(reverse('profiles_index'))
    assert response.status_code == 200
    assert b'john_doe' in response.content

    # Vérifier que la vue de profil contient la ville favorite
    response = client.get(reverse('profile', args=['john_doe']))
    assert response.status_code == 200
    assert b'Paris' in response.content
