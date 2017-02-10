# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 22:18:30 2017

@author: Jean
"""
import numpy as np
from visual.graph import *
import numpy.random as alea
from math import*
from cond_init import*

def acceleration(C,G):
    '''fonction qui calcul l'acceleration de chaque corps à un instant donné
    C est la liste des corps présents
    D est la matrice des distances (D(i,j) correspond a la distance entre le corps i et le corps j))
    A est la matrice des accelerations, de taille n*3 ; chaque ligne i correspond a l'acceleration du corps i
    selon ses trois coordonnées
    '''
    n=len(C)
    D = np.zeros((n, n))
    A = np.zeros((n, 3))
    #remplissage de la matrice D ; calcul de toutes les distances entre tous les corps
    for i in range(n):
        for k in range(n):
            corps1 = C[i]
            corps2 = C[k]
            dx = corps2.x - corps1.x
            dy = corps2.y - corps1.y
            dz = corps2.z - corps1.z
            d2 = dx * dx + dy * dy + dz * dz
            if i == k:
                D[k, i] = 0
            elif sqrt(d2) <= 0.08:  # terme correctif pour éviter l'effet catapulte
                D[k, i] = 0.08
            else:
                D[k, i] = D[i, k] = d2 * sqrt(d2)
    #remplissage de la matrice A
    for i in range(n):
        for k in range(n):
            if k != i:
                corps1 = C[i]
                corps2 = C[k]
                A[i, 0] += G * corps2.m * (corps2.x - corps1.x) / D[i, k] #acceleration du corps i selon x
                A[i, 1] += G * corps2.m * (corps2.y - corps1.y) / D[i, k] #acceleration du corps i selon y
                A[i, 2] += G * corps2.m * (corps2.z - corps1.z) / D[i, k] #acceleration du corps i selon z
    return A

def MAJvitesse(corps, mat,dt):
    '''fonction qui met à jour la vitesse d'un corps à l'instant t+dt
    Prend en argument le corps et la matrice d'accélération'''
    corps.v.x += mat[0] * dt
    corps.v.y += mat[1] * dt
    corps.v.z += mat[2] * dt

def MAJposition(corps,dt):
    '''fonction qui met à jour la position d'un corps, a  l'instant t+dt,
    prend en argument un corps'''
    corps.pos = corps.pos + (corps.v) * dt

def maketrail(Corps,t,dt):
    '''fonction qui permet de d'afficher la trajectoire des corps sur une durée déterminée
    ce qui augmente la   visibilité des trajectoires'''
    if t == t0 + dt:
        for i in Corps:
            i.make_trail = True
            i.trail_type = "curve"
            
def nuageradial(corps, maxi,e):
    '''fonction qui répartit les corps à l'instant initial de façon radial grace
    a la fonction alea de numpy'''
    corps.x = alea.normal(0, maxi) #maxi = longueur du nuage
    corps.y = alea.normal(0, maxi)
    corps.z = alea.normal(0, e)    #e = epaisseur du nuage
    
def vitesseradiale(corps):
    '''fonction qui distribue de façon radiale les vitesse initiales
    plus les étoiles sont loin du centre, plus elles vont lentement comme le dit la 3eme loi de Kepler'''
    d = sqrt(corps.x * corps.x + corps.y * corps.y + corps.z * corps.z)
    vit = sqrt(10*m / (d))  #10 est un facteur correctif pour essayer de reproduire une galaxie
    corps.v = vector(-corps.y / d * vit, corps.x / d * vit, 0)
    
def nbody(Corps,speed,G,dt):
    '''fonction principale qui va effectuer les boucles pour la simulation'''
    t=t0                 #initialisation de t
    n = len(Corps)       #nombre de corps
    ###Vpython settings###
    while True:                     #Tant que la fenêtre n'est pas fermée
        maketrail(Corps, t,dt)         #on dessine la trajectoire du corps
        M = acceleration(Corps,G)     #calcul des accelerations
        t+=dt
        rate(speed)                 #vitesse d'animation (ici limitée par la vitesse de calcul)
        for i in range(n):          
            corps = Corps[i]
            MAJvitesse(corps, M[i],dt)
            MAJposition(corps,dt)