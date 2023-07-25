# projet-13 version pre 17/07/2023
# Mettez à l'échelle une application Django en utilisant une architecture modulaire


<p align="center">
  <a href="https://www.python.org">
    <img src="https://img.shields.io/badge/Python-3.11-2CA5E0?style=flat&logo=python&logoColor=white" alt="python-badge">
  </a>
  <a href="https://www.djangoproject.com">
    <img src="https://img.shields.io/badge/Django-3.0-092E20?style=flat&logo=django&logoColor=white" alt="django-badge">
  </a>
  <a href="https://hub.docker.com/repository/docker/casegibson/oc-p13/">
    <img src="https://img.shields.io/badge/Docker-v24.0.2-2CA5E0?style=flat&logo=docker&logoColor=white" alt="docker-badge">
  </a>
  <a href="https://dashboard.render.com/web/srv-cio5g45ph6ei90e0h65g/">
    <img src="https://img.shields.io/badge/Render-oc--pr--13-ff0000?style=flat&logo=render&logoColor=white" alt="heroku-badge">
  </a>
  <a href="https://none-0cu.sentry.io/issues/">
<img src="https://img.shields.io/badge/Sentry-v1.28.1-2CA5E0?style=flat&logo=sentry&logoColor=white" alt="sentry-badge">  </a>
</p>

## Objectifs du projet 13

1. Réduire la dette technique pour le site web d'Orange County Lettings
- Corriger les erreurs de linting
- Corriger la pluralisation des noms de models

2. Refonte de l'architecture modulaire du site
- Division du site en 3 applications (profiles, lettings et oc_lettings_site)
- Transformer oc_lettings_site en projet django
- Créer divers tests

3. Ajout d'un pipeline CI/CD
- Instaurer des tests (linting, black) en pre-commit
- Executer à nouveau les tests pendant un push
- construire et push une image du site avec Docker (sur dockerhub)
- Déployer le site avec Render

4. Surveillance avec sentry


## Développement local

### Prérequis

Installez la dernière version de python , **disponible** [**ici**](https://www.python.org/downloads/)

Importez le projet depuis git: `git clone https://github.com/thomas-barbato/projet-13.git`

Créez un environnement virtuel :
`python3 -m venv /path/to/new/virtual/environment`
Ou `python -m virtualenv venv`

Activez l'environnement virtuel:
`cd Venv\Scripts\`
`.\activate.bat`
`cd .. `
`cd .. `

Installez les dépendances:
`pip install -r requirements.txt`

#### Linting

- `cd /path/to/projet-13`
- `flake8`

#### Tests unitaires

- `cd /path/to/projet-13`
- `pytest`

#### Base de données

- `cd /projet-13/oc_lettings_site/`
- Ouvrir une session shell:`sqlite3`
- Se connecter à la base de données: `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données: `.tables`
- Afficher les colonnes dans le tableau des profils: `pragma table_info(oc_lettings_site_profile);`
- Lancer une requête sur la table des profils: `select user_id, favorite_city from
  oc_lettings_site_profile where favorite_city like 'B%';`;
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

#### Docker

Pour créer une image docker et la lancer localement

- Téléchargez et installez docker desktop, disponible ici :
  1. **windows**: [**ici**](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module)
  2. **linux**: [**ici**](https://docs.docker.com/desktop/linux/install/)


- Lancez Docker desktop
- Depuis une console dans le répertoire du projet, entrez : `docker build -t nomImage .`
- Pour activer l'image: `docker run --rm -p 8000:8000 --name nomContainer nomImage`\
***attention, nomImage doit être le meme que lors du build.***
- Pour y accéder: http://localhost:8000

Pour créer une image docker et la lancer localement, depuis dockerhub

- Téléchargez et installez docker desktop, disponible ici :
  1. **windows**: [**ici**](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module)
  2. **linux**: [**ici**](https://docs.docker.com/desktop/linux/install/)

- Lancez Docker Desktop
- Depuis une console, entrez : `docker pull casegibson/oc-p13:latest`
- Pour activer l'image: `docker run --rm -p 8000:8000 --name nomContainer casegibson/oc-p13`
- Pour y accéder: http://localhost:8000

## Pre-commit

### Prérequis

Pour activer le pre-commit, vous aurez besoin d'installer les bibliothèques qui y sont liées.

Entrez: `pip install -r requirements-dev.txt`

### Description

Le pre-commit est une série de tests qui surviennent quand on lance un commit, il permet de vérifier
*(selon la configuration choisie)* si ce que vous voulez soumettre est conforme à ce qui est attendu.

### Utilisation manuelle et configuration

Dans le cas où voudriez vous-même tester le bon fonctionnement du pre-commit:

Entrez: `pre-commit --all-files`

Dans le cas où vous voudriez modifier sa configuration,\
modifiez le fichier [.pre-commit-config.yaml](https://github.com/thomas-barbato/projet-13/blob/master/.pre-commit-config.yaml)

## Déploiement

### Prérequis

Pour effectuer le déploiement de l'application, vous aurez besoin de plusieurs comptes :

- [**Github**](https://github.com)
- [**Render**](https://render.com/)
- [**Docker**](https://hub.docker.com/)
- [**Sentry**](https://sentry.io/)

### Description

Le déploiement de l'application est automatisé grace au pipeline CI/CD "github actions - django".
Lorsque l'ont push vers la branche **master**.

**Si les tests sont approuvés** :
- Une image docker est créée
- déploiement vers Render

## Configuration du déploiement
