"""
Ce module contient les vues nécessaires pour rendre la page d'index,
la page d'erreur 404 (non trouvée), et la page d'erreur 500 (erreur interne du serveur).
"""

from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum,
# eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus.
# Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.

def index(request):
    """
    Vue pour rendre la page d'index.
    """
    return render(request, 'index.html')


def custom_page_not_found_view(request, exception=None):
    """
    Vue personnalisée pour gérer les erreurs 404 (Page non trouvée).
    """
    return render(request, '404.html', status=404)


def custom_internal_server_error_view(request):
    """
    Vue personnalisée pour gérer les erreurs 500 (Erreur interne du serveur).
    """
    return render(request, '500.html', status=500)
