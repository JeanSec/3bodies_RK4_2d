# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 22:19:17 2017

@author: Jean
"""


from functions import*
from cond_init import*


'''simulation d'une distribution radiale d'étoile avec distribution radiale des vitesse'''

#initialisation des corps pour affichage
Corps=[]
for i in range(ngala):
    corps = sphere(radius=rayon, make_trail=False, color=color.green,retain=30)
    corps.m = m
    nuageradial(corps,7,1)
    vitesseradiale(corps)
    Corps.append(corps)
    

nbody(Corps,speed0,G1,dt0)