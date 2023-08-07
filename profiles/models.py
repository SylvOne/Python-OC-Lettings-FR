"""
Ce module définit le modèle de profil utilisateur dans notre application.
- Profile: Un profil est lié à un utilisateur
(via une relation OneToOneField avec le modèle User de Django) et contient
des informations supplémentaires telles que la ville favorite de l'utilisateur.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Représente le profil d'un utilisateur, lié à l'objet User de Django par une relation OneToOne.
    Le profil contient des informations supplémentaires sur l'utilisateur,
    telles que sa ville favorite.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles_profile')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
