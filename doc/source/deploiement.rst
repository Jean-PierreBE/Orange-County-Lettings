Déploiement sur un serveur distant
==================================
L'hébergeur choisi pour le déploiement est RENDER.
Les sources :

* packages python
* template html
* fichier css
* dockerfile 
* fichiers de configuration divers

se trouvent dans le repository Github suivant :
https://github.com/Jean-PierreBE/Orange-County-Lettings

Continuous integration
----------------------

Lorsque l'on fait un push ou pull request sur le master 
les contrôles suivants sont lancés

* tests unitaires avec pytest
* flake8
* pylint

si l'exécution s'est déroulée sans erreur , le code est pushé 
dans le cas contraire , une erreur est signalée

Continuous deployment
----------------------

Pour le déploiement , c'est un pull request à partir du master sur la branche prod
qui déclenche le déploiement.

une fois déployé , on peut visualiser le site sur :
https://orange-county-lettings-z6q4.onrender.com
