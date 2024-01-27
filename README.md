# Projet 13 OpenClassRoom : Développez une architecture back-end sécurisée avec Python et SQL
Le but de ce projet est de mettre en place une solution de CRM pour une entreprise organisatrice d'évènements
pour les entreprises. 
Le projet comprend deux parties 
- la partie CRM sous forme d'une API REST écrite avec Django Rest Framework
- la partie ligne de commandes avec Click qui permet d'interagir avec l'API en lignes de commandes

## composition
Tous les fichiers .py necessaires au fonctionnement du logiciel se trouvent dans le répertoire EpicsEvent.
il y a deux sous-répertoires
- src qui contient le code de l'API.
- demo_api qui contient le code click pour faire une démonstration de l'API en ligne de commandes

Les autres fichiers sont :
- README.md qui contient des informations sur le logiciel
- requirements.txt contient les packages necessaires au bon fonctionnement du logiciel
- tox.ini permet de paramétrer flake8 pour voir si le programme répond aux normes pep8

## Installation de l'application
- Cloner le dépôt de code à l'aide de la commande `https://github.com/Jean-PierreBE/EpicsEvent.git`
- Rendez-vous depuis un terminal à la racine du répertoire SoftDesk avec la commande `cd EpicsEvent`
- Créer un environnement virtuel pour le projet avec `$ python -m venv env` sous windows ou `$ python3 -m venv env` sous macos ou linux.
- Activez l'environnement virtuel avec `$ env\Scripts\activate` sous windows ou `$ source env/bin/activate` sous macos ou linux.
- installer les packages python du fichier requirements.txt en lançant la commande suivante 
  - `pip install -r requirements.txt`

## Lancement du programme
Il faut au préalable avoir installé et configuré une base de données PostgreSQL.

Renommer .env.example en .env et remplir les variables.
- Pour créer les tables on tape sur la ligne de commande dans le répertoire src:
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- On lance le programme en tapant sur la ligne de commande dans le répertoire src:
  - `python manage.py runserver`

## Déroulement du programme
Dans le répertoire racine lancer le ou les commandes suivantes
- python -m demo_api users
- python -m demo_api customers
- python -m demo_api contracts
- python -m demo_api events

ces commandes donnent l'aide pour chacune des parties de l'API
Pour chacune de ces parties il est possible de créer , mettre à jour , supprimer , visualiser un ou plusieurs
objets.
Pour la partie user , on a le login et le refresh du token en plus.
ex : on tape `python -m demo_api users create` , le programme invite l'utilisateur à saisir
- son pseudo
- un mot de passe

si l'utilisateur est référencé , un token est généré et l'utilisateur peut saisir les données une par une.
Une fois toutes les données encodées , on fait appel à l'API qui renverra un code retour et un fichier au format 
json le cas échéant. 
Les erreurs d'encodage et fonctionnelles sont affichées également

## Tests
- pour voir si le programme passe les tests unitaires et d'intégration exécuter la commande suivante dans le répertoire src:
  - `pytest --html=test_report.html --self-contained-html`
  - visualiser le fichier test_report.html
- pour voir la couverture des tests lancer la commande suivante :
  - `pytest --cov=. --cov-report html`
  - visualiser le fichier index.html dans le répertoire htmlcov

## Contrôle qualité
Pour vérifier la qualité du code , on peut lancer le commandes suivantes :
- `flake8 --format=html --htmldir=flake-report src`
- `flake8 --format=html --htmldir=flake-report-click demo_api`
Les rapports sortiront en format html dans les répertoires 
- flake-report
- flake-report-click

pour cela il faut installer :
- flake8 : contrôle du code pour vérifier la compatibilité avec les normes pep8
- flake8-html : permet de sortir le rapport flake8 sous format html
- flake8-functions : permet d'ajouter des contrôles au niveau des fonctions (ex : longueur maximale des fonctions)

le fichier tox.ini contient la configuration pour flake8.
- `exclude = migrations` : la longueur maximale de chaque ligne ne peut pas dépasser 119 caractères
- `max-line-length = 120` : la longueur maximale de chaque ligne ne peut pas dépasser 119 caractères
- `max-function-length = 50` : la longueur maximale de chaque fonction ne peut pas dépasser 50 lignes
- `ignore = CFQ002, CFQ004, W503, W504` : évite les erreurs
  - CFQ002 : nombre d'arguments en entrée trop élevés (> 6)
  - CFQ004 : nombre d'éléments en retour trop élevés (> 3)
  - W503 : saut de ligne avant un opérateur
  - W504 : saut de ligne après un opérateur

Ces paramètres peuvent être modifiés

