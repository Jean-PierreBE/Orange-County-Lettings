# Projet 13 OpenClassRoom : Mettez à l'échelle une application Django en utilisant une architecture modulaire
Le but de ce projet est d'améliorer un projet existant
- de créer une architecture modulaire
- de réduire la dette technique
- mettre en place ube série de tests
- documenter le code
- automatiser l'intégration et le déploiement
- mettre à disposition une documentation technique
Le readme explique essentiellement l'installation en local
Pour avoir une documentation plus complète , notamment sur le déploiement sur un serveur veuillez consulter
 `https://orange-county-lettings-documentation.readthedocs.io/fr/latest/`
## composition
Tous les fichiers .py necessaires au fonctionnement de l'application se trouvent dans le répertoire Orange-County-Lettings.

Les autres fichiers sont :
- README.md qui contient des informations sur le logiciel
- requirements.txt contient les packages necessaires au bon fonctionnement du logiciel
- setup.cfg qui contient les paramètres pour flake8, pytest , pylint
- la db sqlite3

## Installation de l'application en local
- Cloner le dépôt de code à l'aide de la commande `https://github.com/Jean-PierreBE/Orange-County-Lettings.git`
- Rendez-vous depuis un terminal à la racine du répertoire Orange-County-Lettings avec la commande `cd Orange-County-Lettings`
- Créer un environnement virtuel pour le projet avec `$ python -m venv env` sous windows ou `$ python3 -m venv env` sous macos ou linux.
- Activez l'environnement virtuel avec `$ env\Scripts\activate` sous windows ou `$ source env/bin/activate` sous macos ou linux.
- installer les packages python du fichier requirements.txt en lançant la commande suivante 
  - `pip install -r requirements.txt`

## Lancement du programme
Renommer .env.example en .env et remplir les variables.
- Pour créer les tables on tape sur la ligne de commande dans le répertoire src:
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- On lance le programme en tapant sur la ligne de commande dans le répertoire src:
  - `python manage.py runserver`

## Déroulement du programme
le site s'affiche. Pour avoir une explication plus détaillée consulter 
`https://orange-county-lettings-documentation.readthedocs.io/fr/latest/manuel.html`

## Contrôle qualité
Pour vérifier la qualité du code , on peut lancer le commandes suivantes :
- `flake8 --format=html --htmldir=flake-report`
Les rapports sortiront en format html dans le répertoire flake-report

pour cela il faut installer :
- flake8 : contrôle du code pour vérifier la compatibilité avec les normes pep8
- flake8-html : permet de sortir le rapport flake8 sous format html

le fichier setu.cfg contient la configuration pour flake8.
- `exclude = **/migrations/*,venv` : ne contrôle pas les fichiers dans les répertoires migrations et venv
- `max-line-length = 99` : la longueur maximale de chaque ligne ne peut pas dépasser 99 caractères
Ces paramètres peuvent être modifiés

On peut lancer également pylint pour détecter des bugs , contrôler la présence de doc string
Pour cela lancer la commande `pylint`



