"""
Ce module définit les modèles pour les adresses et les locations.
Il contient deux classes principales:

- Address: représente une adresse postale avec des champs pour le numéro, la rue, la ville,
  l'État, le code postal, et le code ISO du pays.
- Letting: représente une location, liée à une adresse par une relation OneToOneField.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """ Représente une adresse postale """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """ Représente une location liée à une adresse """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
