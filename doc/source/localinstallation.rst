Installation en local du projet
===============================

Installation
------------

* Cloner le dépôt de code à l'aide de la commande https://github.com/Jean-PierreBE/Orange-County-Lettings.git
* Rendez-vous depuis un terminal à la racine du répertoire Orange-County-Lettings avec la commande cd Orange-County-Lettings
* Créer un environnement virtuel pour le projet avec $ python -m venv env sous windows ou $ python3 -m venv env sous macos ou linux.
* Activez l'environnement virtuel avec $ env\Scripts\activate sous windows ou $ source env/bin/activate sous macos ou linux.
* installer les packages python du fichier requirements.txt en lançant la commande suivante pip install -r requirements.txt

Lancement
---------

* Renommer .env.example en .env et remplir les variables.

* Pour créer les tables on tape sur la ligne de commande dans le répertoire Orange-County-Lettings:

	* python manage.py makemigrations
	* python manage.py migrate
	
* On lance le programme en tapant sur la ligne de commande dans le répertoire Orange-County-Lettings: python manage.py runserver

