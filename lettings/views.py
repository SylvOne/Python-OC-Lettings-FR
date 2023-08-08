"""
Ce module gère les vues pour la section des locations de l'application.
Il contient des vues pour lister toutes les locations
et afficher les détails d'une location individuelle.

Fonctions:
    index(request): Renvoie une liste de toutes les locations.
    letting(request, letting_id): Renvoie les détails d'une location individuelle par son ID.
"""

from django.shortcuts import render
from .models import Letting
from django.http import Http404
import logging


logger = logging.getLogger(__name__)

# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa. Integer est nunc, pulvinar a tempor et,
# bibendum id arcu. Vestibulum ante ipsum primis in faucibus orci luctus et
# ultrices posuere cubilia curae; Cras eget scelerisque


def index(request):
    """
    Renvoie une vue avec une liste de toutes les locations disponibles.

    Args:
        request (HttpRequest): L'objet requête de la vue.

    Returns:
        HttpResponse: Une réponse contenant le rendu de la liste des locations.
    """
    try:
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        logger.error(f"An error occurred while retrieving the lettings: {str(e)}")


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend. Praesent dignissim,
# odio eu consequat pretium, purus urna vulputate arcu,
# vitae efficitur lacus justo nec purus.
# Aenean finibus faucibus lectus at porta.
# Maecenas auctor, est ut luctus congue, dui enim mattis enim,
# ac condimentum velit libero in magna. Suspendisse potenti. In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum.
# Ut quis urna pellentesque justo mattis ullamcorper ac non tellus.
# In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem.
# Sed non dolor risus. Mauris condimentum auctor elementum.
# Donec quis nisi ligula. Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.

def letting(request, letting_id):
    """
    Renvoie une vue avec les détails d'une location individuelle.

    Args:
        request (HttpRequest): L'objet requête de la vue.
        letting_id (int): L'ID de la location à afficher.

    Returns:
        HttpResponse: Une réponse contenant le rendu des détails de la location.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:
        logger.error(f"Letting with ID {letting_id} not found.")
        raise Http404("Profile not found.")
