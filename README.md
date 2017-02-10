Environnement requis pour l'execution des scripts:
python 2.7 + anaconda + Vpython.
En particulier, dans anaconda, nous utiliserons scipy/matplotlib/numpy

###liens de download###
http://vpython.org/
https://www.continuum.io/downloads
#######################

Nous avons utilisé spyder2.7 qui se trouve fournie dans anaconda.

Organisation des fichiers:
A chaque dossier correspond :
	-une méthode de résolution différente ou
	-une dimension de l'espace différente ou
	-un nombre de corps différent
En 2d nous utilisons matplotlib, en 3d nous utilisons Vpython

Dans le dossier nbodies_euler3D, le script a été un peu plus long que les autres, nous l'avons donc scindé en plusieurs parties:
	-une partie functions qui contient toutes les procédures.
	-une partie condition initiales qui contient tous les paramètres qui varient à chaque simulation différente
	-plusieurs parties 'main' qui correspondent chacune à une simulation différente

Nous contacter : jpl96@orange.fr
