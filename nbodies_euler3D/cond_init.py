# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 22:20:06 2017

@author: Jean
"""
from visual import *

'''définition des conditions initiales et des paramètres du système pour plusieurs cas'''

speed=1000                #vitesse de la simulation, limité par le temps de calcul
scene.fov = pi / 2        #angle de vision maximum

# définition des paramètres
G = 1          # constante gravitationnelle
dt0 = 0.01     # pas de temps
dt1=3600       #deuxieme pas de temps disponible
dt2=0.2*10**-4
rayon = 0.15   #rayon visible des corps sur l interface graphique
t0 = 0         #instant initial
m = 1          #masse des corps
ngala=70       #nombre de corps dans la galaxie
speed0=1000    #vitesse d'animation de la galaxie
speed1=100     #vitesse d'animation des 3 corps
speed2=500     #↓vitesse d'animation du système solaire
speed3=10000
G1=1
G0=6.67384 * 10 ** -11 


