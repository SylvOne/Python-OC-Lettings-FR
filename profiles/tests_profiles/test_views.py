"""
Module de tests pour les vues de l'application "Profiles".
Ces tests vérifient les réponses des vues, y compris les codes de statut HTTP.
"""

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_index_view(client):
    """
    Teste la vue de l'index des profils.
    Vérifie que la page d'index est accessible et renvoie un code de statut HTTP 200.
    """
    response = client.get(reverse('profiles_index'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view(client):
    """
    Teste la vue du profil individuel.
    Vérifie que la page de profil est accessible pour un utilisateur spécifique
    et renvoie un code de statut HTTP 200.
    """
    user = User.objects.create(username='john_doe')
    Profile.objects.create(user=user, favorite_city='Paris')
    response = client.get(reverse('profile', args=['john_doe']))
    assert response.status_code == 200
