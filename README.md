## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/SylvOne/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`
- `pystest --cov`

##### Tests lettings app

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest lettings/tests_lettings --cov=lettings`

##### Tests profiles app

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest profiles/tests_profiles --cov=profiles`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Déploiement

#### Récapitulatif du fonctionnement du déploiement

Le déploiement est effectué à l'aide d'un pipeline CI/CD, orchestré avec CircleCI, qui teste, conteneurise et déploie l'application sur AWS. Le pipeline inclut des étapes pour la vérification du style de code, l'exécution de tests unitaires, la construction d'images Docker, le push des images vers AWS ECR et Docker Hub, et le déploiement sur AWS Elastic Beanstalk.

#### Configuration requise

Assurez-vous que les variables d'environnement suivantes sont configurées dans CircleCI :

- `SECRET_KEY`
- `SENTRY_DSN`
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `DJANGO_DEBUG`
- `AWS_REGION`
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_PASSWORD`
- `APP_AWS`
- `APP_ENVIRONNEMENT_AWS`
- `S3_BUCKET_DOCKRUN`
- `DOCKERRUN`

#### Étapes nécessaires pour effectuer le déploiement

<b>À noter</b> : 

La phase de déploiement sera executée uniquement lors d'un "push" github vers la branche principale. Lors d'un push github sur une branche secondaire seul la phase de tests de conformité PEP8 et de tests unitaires sera executée.

1. **Tests de toutes les branches**: Exécution de tests de conformité PEP8 et de tests unitaires.
2. **Conteneurisation et déploiement**:
   - Construction de l'image Docker avec les variables de build.
   - Marquage et push de l'image vers AWS ECR et Docker Hub.
   - Synchronisation des fichiers statiques avec S3.
   - Déploiement de l'application sur Elastic Beanstalk.

Ces étapes sont automatiquement gérées par le fichier de configuration CircleCI (config.yml). Aucune intervention manuelle n'est nécessaire si les configurations sont correctement définies.

### Exécuter l'image Docker en local

Pour exécuter l'image Docker de ce projet localement, vous pouvez utiliser le script `run_container.sh` fourni. Voici les étapes à suivre :

#### Configuration des variables d'environnement
Assurez-vous que le fichier `.env` contient les variables d'environnement correctes. Voici les variables nécessaires :
```
SENTRY_DSN=your-sentry-dsn
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
AWS_STORAGE_BUCKET_NAME=your-storage-bucket-name
DJANGO_DEBUG=True-or-False
```

#### Rendre le script exécutable

Dans votre terminal, naviguez jusqu'au répertoire où se trouve le fichier run_container.sh et exécutez la commande suivante pour le rendre exécutable :

```
chmod +x run_container.sh
```

#### Exécution du script

Lancez le script avec la commande suivante :

```
./run_container.sh
```

Ce script effectue les actions suivantes :

* Se connecte à Docker Hub en utilisant vos identifiants.
* Télécharge l'image Docker la plus récente du registre Docker Hub.
* Lance l'image en tant que conteneur avec les variables d'environnement spécifiées et expose le port 8000.

#### Accéder à l'application

Une fois le conteneur lancé, vous pouvez accéder à l'application en ouvrant votre navigateur web et en allant à http://localhost:8000.

Assurez-vous d'avoir Docker installé sur votre système et que vous êtes connecté à Internet pour pouvoir télécharger l'image depuis Docker Hub.
