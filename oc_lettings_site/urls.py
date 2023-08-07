"""
Ce module définit les chemins URL principaux pour le projet. Il inclut les chemins URL
des modules lettings et profiles, et définit également les gestionnaires personnalisés
pour les erreurs 404 (Page non trouvée) et 500 (Erreur interne du serveur).

- `index`: La page d'accueil du site.
- `lettings/`: Les chemins URL associés aux annonces immobilières.
- `profiles/`: Les chemins URL associés aux profils des utilisateurs.
- `admin/`: L'interface d'administration de Django.
"""

from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include("lettings.urls"), name='lettings'),
    path('profiles/', include("profiles.urls"), name='profiles'),
    path('admin/', admin.site.urls),
]

# Gestion des erreurs 404 et 500
handler404 = 'oc_lettings_site.views.custom_page_not_found_view'
handler500 = 'oc_lettings_site.views.custom_internal_server_error_view'
