.. OC Lettings documentation master file, created by
   sphinx-quickstart on Fri Aug 11 13:25:13 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=================================
Site web d'Orange County Lettings
=================================

1. Description du Projet
========================

Projet: Site web d'Orange County Lettings.

Le projet a pour but de créer une plateforme de location pour Orange County Lettings. Il utilise des technologies telles que Python, SQLite3, et Django, et suit les principes de développement CI/CD.

2. Instructions sur l’Installation du Projet
=============================================

Développement local :

Prérequis
'''''''''
- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

macOS / Linux
'''''''''''''

1. **Cloner le repository:**

.. code-block:: bash

      cd /path/to/put/project/in
      git clone https://github.com/SylvOne/Python-OC-Lettings-FR.git

2. **Créer l'environnement virtuel:**

.. code-block:: bash

      cd /path/to/Python-OC-Lettings-FR
      python -m venv venv
      apt-get install python3-venv (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
      Activer l'environnement source venv/bin/activate
      Confirmer que la commande python exécute l'interpréteur Python dans l'environnement virtuel which python
      Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure python --version
      Confirmer que la commande pip exécute l'exécutable pip dans l'environnement virtuel, which pip
      Pour désactiver l'environnement, deactivate

Windows
''''''''
Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, .\venv\Scripts\Activate.ps1
- Remplacer which <my-command> par (Get-Command <my-command>).Path


3. Guide de Démarrage Rapide (Instructions pour le déploiement)
===============================================================

- Après avoir cloné le projet, suivez les instructions d'installation.

.. code-block:: bash

      cd /path/to/Python-OC-Lettings-FR
      source venv/bin/activate
      pip install --requirement requirements.txt
      python manage.py runserver

- Naviguez sur http://localhost:8000 dans un navigateur.
- Vérifiez que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).
- Aller sur le pannel d'administration http://localhost:8000/admin et connectez-vous avec l'utilisateur "admin" , mot de passe Abc1234!


4. Technologies et Langages de Programmation Utilisés
=====================================================
- **Langages de Programmation:** Python (3.9)
- **Framework:** Django
- **Base de Données:** SQLite3
- **Outils de CI/CD:** CircleCI, AWS, GitHub
- **Outils de containerisation:** Docker
- **Outils de linting:** Flake8
- **Outils de tests:** Pytest


5. Structure de la Base de Données et des Modèles de Données
=============================================================

La structure de la base de données pour le projet Django en question se compose de 2 applications : `profiles` et `lettings`.

Application Lettings
'''''''''''''''''''''

Cette application gère les locations et les adresses.

**Modèle Address:**
   La table `Address` stocke les adresses postales.

   - `number`: Un champ entier positif pour le numéro de l'adresse, limité à 9999.
   - `street`: Un champ de caractères pour le nom de la rue, limité à 64 caractères.
   - `city`: Un champ de caractères pour la ville, limité à 64 caractères.
   - `state`: Un champ de caractères pour l'état, exactement 2 caractères.
   - `zip_code`: Un champ entier positif pour le code postal, limité à 99999.
   - `country_iso_code`: Un champ de caractères pour le code ISO du pays, exactement 3 caractères.

**Modèle Letting:**
   La table `Letting` représente les locations.

   - `title`: Un champ de caractères pour le titre de la location, limité à 256 caractères.
   - `address`: Une relation OneToOne avec la table `Address`, liant chaque location à une adresse.

Application Profiles
'''''''''''''''''''''

Cette application gère les profils utilisateurs.

**Modèle Profile:**
   La table `Profile` est liée aux utilisateurs.

   - `user`: Une relation OneToOne avec la table `User` de Django, liant chaque profil à un utilisateur.
   - `favorite_city`: Un champ de caractères pour la ville favorite de l'utilisateur, limité à 64 caractères et pouvant être vide.

Relation entre les Tables
'''''''''''''''''''''''''

Les tables sont reliées comme suit :

- La table `Address` est reliée à la table `Letting` via une relation OneToOne, où chaque location possède une adresse.
- La table `Profile` est reliée à la table `User` de Django via une relation OneToOne, où chaque utilisateur possède un profil.

6. Guide d'Utilisation (Cas d'Utilisation)
==========================================

- **Cas d'Utilisation 1: Naviguer sur la Page d'Accueil**

   **Acteur:** Visiteur

   **But:** Accéder aux sections principales du site.

   **Préconditions:** Le visiteur a accédé au site web.

   **Déroulement principal:**

   * Le visiteur peut cliquer sur le lien "Profiles" pour voir la liste des profils.

   * Le visiteur peut cliquer sur le lien "Lettings" pour voir les offres de location.

   **Postconditions:** Le visiteur a accès aux sections principales du site.

- **Cas d'Utilisation 2: Voir les Profils**

   **Acteur:** Visiteur

   **But:** Voir la liste des profils disponibles sur le site.

   **Préconditions:** Le visiteur est sur la page "Profiles".

   **Déroulement principal:**

   * Le visiteur peut cliquer sur un nom de profil pour voir les détails.

   **Postconditions:** Le visiteur peut voir la liste des profils et accéder aux détails de chacun.


- **Cas d'Utilisation 3: Voir les Lettings (Locations)**

   **Acteur:** Visiteur

   **But:** Voir la liste des locations disponibles sur le site.

   **Préconditions:** Le visiteur est sur la page "Lettings".

   **Déroulement principal:**

   * Le visiteur peut cliquer sur un nom de location pour voir les détails.

   **Postconditions:** Le visiteur peut voir la liste des locations et accéder aux détails de chacun.


- **Cas d'Utilisation 4: Navigation entre les Pages**

   **Acteur:** Visiteur

   **But:** Permettre une navigation facile entre différentes sections du site.

   **Préconditions:** Le visiteur est sur l'une des pages du site.

   **Déroulement principal:**

   * Le visiteur peut naviguer entre la page d'accueil, la page de profil et la page de lettings en utilisant les boutons ou liens correspondants.
   
   **Postconditions:** Le visiteur a accédé à la page souhaitée.


- **Cas d'Utilisation 5: Connexion à l'Espace Administrateur**

   **Acteur:** Administrateur

   **But:** Permettre à l'administrateur de s'authentifier et d'accéder à l'espace d'administration.

   **Préconditions:**

   * L'administrateur a un compte valide avec des privilèges d'administration.

   **Déroulement principal:**

   * L'administrateur ouvre la page de connexion.

   * L'administrateur saisit son nom d'utilisateur et son mot de passe.

   * L'administrateur clique sur le bouton "Connexion".

   * Le système valide les informations d'identification et accorde l'accès à l'espace d'administration si elles sont correctes.

   **Déroulement alternatif :** Suppression de l'accès à un administrateur

   * Un super-administrateur ouvre la page de gestion des administrateurs.

   * Il sélectionne un administrateur spécifique.

   * Il clique sur le bouton "Supprimer" pour révoquer les privilèges d'administration de cet administrateur.

   **Postconditions:**

   * Si la connexion réussit, l'administrateur est connecté et a accès aux fonctionnalités d'administration.

   * Si la suppression réussit, l'administrateur sélectionné n'a plus accès à l'espace d'administration.


- **Cas d'Utilisation 6: Gestion des Utilisateurs**

   **Acteur:** Administrateur

   **But:** Permettre à l'administrateur d'ajouter, modifier, visualiser et supprimer les utilisateurs.

   **Préconditions:** L'administrateur est connecté à la page d'administration.

   **Déroulement principal:**

   * L'administrateur peut cliquer sur "Users" pour visualiser la liste des utilisateurs.

   * L'administrateur peut cliquer sur "Add" pour ajouter un nouvel utilisateur.

   * L'administrateur peut cliquer sur "Change" pour modifier un utilisateur existant.

   * L'administrateur peut cliquer sur "Delete" pour supprimer un utilisateur existant.

   **Postconditions:** Les modifications souhaitées sont apportées aux utilisateurs.


- **Cas d'Utilisation 7: Gestion des Adresses**

   Acteur: Administrateur

   **But:** Permettre à l'administrateur d'ajouter, modifier, visualiser et supprimer les adresses.

   **Préconditions:** L'administrateur est connecté à la page d'administration.

   **Déroulement principal:**

   * L'administrateur peut cliquer sur "Addresses" pour visualiser la liste des adresses.

   * L'administrateur peut cliquer sur "Add" pour ajouter une nouvelle adresse.

   * L'administrateur peut cliquer sur "Change" pour modifier une adresse existante.

   * L'administrateur peut cliquer sur "Delete" pour supprimer une adresse existante.

   **Postconditions:** Les modifications souhaitées sont apportées aux adresses.


- **Cas d'Utilisation 8: Gestion des Profils**

   **Acteur:** Administrateur

   **But:** Permettre à l'administrateur d'ajouter, modifier, visualiser et supprimer les profils.

   **Préconditions:** L'administrateur est connecté à la page d'administration.

   **Déroulement principal:**

   * L'administrateur peut cliquer sur "Profiles" pour visualiser la liste des profils.

   * L'administrateur peut cliquer sur "Add" pour ajouter un nouveau profil.

   * L'administrateur peut cliquer sur "Change" pour modifier un profil existant.

   * L'administrateur peut cliquer sur "Delete" pour supprimer un profil existant.

   **Postconditions:** Les modifications souhaitées sont apportées aux profils.

- **Cas d'Utilisation 9: Gestion des Locations (Lettings)**

   **Acteur:** Administrateur

   **But:** Permettre à l'administrateur d'ajouter, modifier, visualiser et supprimer les locations.

   **Préconditions:** L'administrateur est connecté à la page d'administration.

   **Déroulement principal:**

   * L'administrateur peut cliquer sur "Lettings" pour visualiser la liste des locations.

   * L'administrateur peut cliquer sur "Add" pour ajouter une nouvelle location.

   * L'administrateur peut cliquer sur "Change" pour modifier une location existante.

   * L'administrateur peut cliquer sur "Delete" pour supprimer une location existante.

   **Postconditions:** Les modifications souhaitées sont apportées aux locations.



7. Interfaces de Programmation des Applications Lettings et Profiles
====================================================================

Application : Lettings
'''''''''''''''''''''''

L'application "lettings" gère tout ce qui concerne les locations.

Modèles
^^^^^^^

   Address:
      - **Champs**: number, street, city, state, zip_code, country_iso_code.
      - **Relations**: Aucune.
      - **Description**: Utilisé pour stocker les adresses des locations.

   Letting:
      - **Champs**: title, address.
      - **Relations**: Relié à Address par une relation OneToOneField.
      - **Description**: Utilisé pour représenter une location immobilière.

Vues
^^^^

   - **index**: Affiche une liste des locations.
   - **letting**: Affiche les détails d'une location spécifique.

Urls
^^^^

   - **lettings_index**: Chemin vers l'index des locations.
   - **letting**: Chemin vers la vue de détail d'une location individuelle.

Admin
^^^^^

   - **Address**: Les administrateurs peuvent créer, modifier, supprimer des adresses.
   - **Letting**: Les administrateurs peuvent créer, modifier, supprimer des locations.



Application : Profiles
'''''''''''''''''''''''

L'application "profiles" gère tout ce qui concerne les profils des utilisateurs.

Modèles
^^^^^^^

   Profile:
      - **Champs**: user, favorite_city.
      - **Relations**: Lié à l'objet User de Django par une relation OneToOne.
      - **Description**: Représente le profil d'un utilisateur.

Vues
^^^^

   - **index**: Vue pour lister tous les profils d'utilisateurs.
   - **profile**: Vue pour afficher un profil spécifique.

Urls
^^^^
   - **profiles_index**: Chemin vers l'index des profils d'utilisateurs.
   - **profile**: Chemin vers la vue de détail d'un profil individuel.

Admin
^^^^^

   - **Profile**: Les administrateurs peuvent créer, modifier, supprimer des profils.



Répertoire Principal : oc_lettings_site
'''''''''''''''''''''''''''''''''''''''

Vues
^^^^

   - **index**: Vue pour rendre la page d'index.
   - **custom_page_not_found_view**: Vue personnalisée pour gérer les erreurs 404 (Page non trouvée).
   - **custom_internal_server_error_view**: Vue personnalisée pour gérer les erreurs 500 (Erreur interne du serveur).

Urls
^^^^

   - **index**: La page d'accueil du site.
   - **lettings**: Les chemins URL associés aux annonces immobilières.
   - **profiles**: Les chemins URL associés aux profils des utilisateurs.
   - **admin**: L'interface d'administration de Django.

Gestionnaires d'Erreur
^^^^^^^^^^^^^^^^^^^^^^

   - **handler404**: Gestion des erreurs 404 (Page non trouvée).
   - **handler500**: Gestion des erreurs 500 (Erreur interne du serveur).


8. Procédures de déploiement
============================

Récapitulatif du fonctionnement du déploiement
'''''''''''''''''''''''''''''''''''''''''''''''
Le déploiement est effectué à l'aide d'un pipeline CI/CD, orchestré avec CircleCI, qui teste, conteneurise et déploie l'application sur AWS. Le pipeline inclut des étapes pour la vérification du style de code, l'exécution de tests unitaires, la construction d'images Docker, le push des images vers AWS ECR et Docker Hub, et le déploiement sur AWS Elastic Beanstalk.

Configuration requise
'''''''''''''''''''''

Assurez-vous que les variables d'environnement suivantes sont configurées dans CircleCI:

- SECRET_KEY
- SENTRY_DSN
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- DJANGO_DEBUG
- AWS_REGION
- DOCKERHUB_USERNAME
- DOCKERHUB_PASSWORD
- APP_AWS
- APP_ENVIRONNEMENT_AWS
- S3_BUCKET_DOCKRUN
- DOCKERRUN

Étapes nécessaires pour effectuer le déploiement
''''''''''''''''''''''''''''''''''''''''''''''''''
**À noter:**

La phase de déploiement sera executée uniquement lors d'un "push" github vers la branche principale. 

Lors d'un push github sur une branche secondaire seul la phase de tests de conformité PEP8 et de tests unitaires sera executée.

- **Tests effectué sur toutes les branches:** 

   Exécution de tests de conformité PEP8 et de tests unitaires.

- **Conteneurisation et déploiement:** ( uniquement effectué sur la branche principale )

   - Construction de l'image Docker avec les variables de build.
   - Marquage et push de l'image vers AWS ECR et Docker Hub.
   - Synchronisation des fichiers statiques avec S3.
   - Déploiement de l'application sur Elastic Beanstalk.

   Ces étapes sont automatiquement gérées par le fichier de configuration CircleCI (config.yml).

   Aucune intervention manuelle n'est nécessaire si les configurations sont correctement définies.


Exécuter l'image Docker en local
''''''''''''''''''''''''''''''''
Pour exécuter l'image Docker de ce projet localement, vous pouvez utiliser le script ``run_container.sh`` fourni. Voici les étapes à suivre:

1. **Configuration des variables d'environnement**

   - SENTRY_DSN=your-sentry-dsn
   - AWS_ACCESS_KEY_ID=your-access-key-id
   - AWS_SECRET_ACCESS_KEY=your-secret-access-key
   - AWS_STORAGE_BUCKET_NAME=your-storage-bucket-name
   - DJANGO_DEBUG=True-or-False

2. **Rendre le script exécutable**

   ``chmod +x run_container.sh``

3. **Exécution du script**

   ``./run_container.sh``

   Ce script effectue les actions suivantes :

   - Se connecte à Docker Hub en utilisant vos identifiants.
   - Télécharge l'image Docker la plus récente du registre Docker Hub.
   - Lance l'image en tant que conteneur avec les variables d'environnement spécifiées et expose le port 8000.

4. **Accéder à l'application**

   Une fois le conteneur lancé, vous pouvez accéder à l'application en ouvrant votre navigateur web et en allant à http://localhost:8000.

   Assurez-vous d'avoir Docker installé sur votre système et que vous êtes connecté à Internet pour pouvoir télécharger l'image depuis Docker Hub.


9. Surveillance et Gestion des Erreurs avec Sentry
==================================================

Notre application utilise Sentry pour surveiller et gérer les erreurs.

Sentry aide à capturer et signaler les exceptions en temps réel, permettant une réponse rapide et une résolution des problèmes.


Configuration dans ``settings.py``
''''''''''''''''''''''''''''''''''

La configuration de Sentry dans notre application est définie dans le fichier ``settings.py``.

Sentry a été configuré pour capturer les messages de niveau ``INFO`` et les erreurs de niveau ``ERROR``. Voici un aperçu de la configuration :

.. code-block:: python

   sentry_logging = LoggingIntegration(
       level=logging.INFO,
       event_level=logging.ERROR
   )

   sentry_sdk.init(
       dsn=SENTRY_DSN,
       integrations=[DjangoIntegration(), sentry_logging],
       traces_sample_rate=1.0,
       send_default_pii=True
   )

Intégration dans les Vues de l'Application
''''''''''''''''''''''''''''''''''''''''''''

Sentry est utilisé dans les modules suivants de notre application :

App Lettings
'''''''''''''

Ce module gère les locations et contient des vues pour lister toutes les locations et afficher les détails d'une location individuelle. Sentry est utilisé pour logger les erreurs lors de la récupération des locations.

- ``index(request)``: Log les erreurs lors de la récupération de la liste des locations.
- ``letting(request, letting_id)``: Log les erreurs lors de la récupération des détails d'une location spécifique.

App Profiles
'''''''''''''

Ce module gère les profils des utilisateurs. Sentry est utilisé pour logger les erreurs lors de la récupération des profils.

- ``index(request)``: Log les erreurs lors de la récupération de la liste des profils.
- ``profile(request, username)``: Log les erreurs lors de la récupération d'un profil spécifique.

Vues de ``oc_lettings_site``
''''''''''''''''''''''''''''

Ce module gère les vues principales de l'application, y compris les erreurs 404 et 500.

- ``custom_page_not_found_view(request, exception=None)``: Log les erreurs 404.
- ``custom_internal_server_error_view(request)``: Log les erreurs 500.

Conclusion
'''''''''''

L'intégration de Sentry dans notre application Django permet une surveillance continue des erreurs et des exceptions. Cela facilite la détection rapide des problèmes et aide l'équipe de développement à maintenir la stabilité et la qualité de l'application.
