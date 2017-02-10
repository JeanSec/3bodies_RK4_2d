from visual import *
import thread
import numpy as np
from visual.graph import *
from math import *
import wx
import os
import sys
'''ce programme calcul les trajectoires de 3 corps en interactions gravitaionelle grace a la m�thode
d'Euler, en temps reel, 
et les affiche en 3D grace au module Vpython. Un graphique d energie mecanique
du systeme est egalement affich� en temps reel.
On peut se d�placer dans la fene�tre a l'aide de la souris et 
du clic droit'''

def acceleration(C):
    global G
    '''fonction qui calcul l'acceleration de chaque corps � un instant donn�
    C est la liste des corps pr�sents
    D est la matrice des distances (D(i,j) correspond a la distance entre le corps i et le corps j))
    A est la matrice des accelerations, de taille n*3 ; chaque ligne i correspond a l'acceleration du corps i
    selon ses trois coordonn�es
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

def MAJvitesse(corps, mat):
    global dt
    '''fonction qui met � jour la vitesse d'un corps � l'instant t+dt
    Prend en argument le corps et la matrice d'acc�l�ration'''
    corps.v.x += mat[0] * dt
    corps.v.y += mat[1] * dt
    corps.v.z += mat[2] * dt

def MAJposition(corps):
    global dt
    '''fonction qui met � jour la position d'un corps, a  l'instant t+dt,
    prend en argument un corps'''
    corps.pos = corps.pos + (corps.v) * dt

def maketrail(Corps,t):
    '''fonction qui permet de d'afficher la trajectoire des corps sur une dur�e d�termin�e
    ce qui augmente la   visibilit� des trajectoires'''
    global dt
    if t == t0 + dt:
        for i in Corps:
            i.make_trail = True
            i.trail_type = "curve"
            
def ENmeca(C):
    '''fonction qui calcul l'�nergie mecanique du systeme � un instant t'''
    E = 0
    for i in range(len(C)):
        corps0 = C[i]
        E += (corps0.v.x ** 2 + corps0.v.y ** 2 + corps0.v.z ** 2) * corps0.m * 0.5 #energie cinetique
        for k in range(len(C)):
            corps1 = C[k]
            if i != k:
                #calcul des distances
                dx = corps1.x - corps0.x
                dy = corps1.y - corps0.y
                dz = corps1.z - corps0.z
                d = sqrt(dx * dx + dy * dy + dz * dz)
                E -= 0.5*G * corps0.m * corps1.m / d                               #energie potentielle gravitationelle
    return E

def initgraph(colorg):
    '''fonction pour tracer le graphique d energie mecanique en temps reel'''
    global f1
    f1 = gcurve(color=colorg)

def newpointgraph(t,k,Corps,p):
    '''fonction pour tracer le graphique d energie mecanique en temps reel'''
    if k%p == 0:
        f1.plot(pos=(t, ENmeca(Corps)))

speed=100                   #vitesse de la simulation, limit� par le temps de calcul
scene.scale=(0.1,0.1,0.1)   #zoom initial sur la scene
scene.title = "3 corps"
scene.fov = pi / 2          #angle de vision maximum

# d�finition des param�tres
G = 1          # constante gravitationnelle
dt = 0.01      # pas de temps
rayon = 0.05   #rayon visible des corps sur l interface graphique
t0 = 0         #instant initial

###Affichage###
#initialisation des corps
corps0 = sphere(radius=rayon, make_trail=False, color=color.cyan,retain=210000)
corps1 = sphere(radius=rayon, make_trail=False, color=color.white,retain=210000)
corps2 = sphere(radius=rayon, make_trail=False, color=color.red,retain=100000)

#initialisation des masses
corps0.m = 1
corps1.m = 1
corps2.m = 0.01

###initialisation des vitesses
corps0.v = vector(0, 0.25,0)
corps1.v = vector(0, -0.25,0)
corps2.v = vector(0, 0, 1.3)

###initialisation des positions
corps0.x, corps0.y, corps0.z = 1, 0, 0
corps1.x, corps1.y, corps1.z = -1, 0, 0
corps2.x, corps2.y, corps2.z = 0, 0, 0

Corps = [corps0, corps1, corps2]

def nbody(Corps):
    '''fonction principale qui va effectuer les boucles pour la simulation'''
    k=0                  #initialisation de k qui va servir � afficher le graph
    t=t0                 #initialisation de t
    initgraph(color.red) #initialisation du graph
    n = len(Corps)       #nombre de corps
    ###Vpython settings###
    while True:                     #Tant que la fen�tre n'est pas ferm�e
        maketrail(Corps, t)         #on dessine la trajectoire du corps
        M = acceleration(Corps)     #calcul des accelerations
        newpointgraph(t,k,Corps,20) #nouveau point sur le graph toutes les 20 it�rations
        t+=dt
        k+=1
        rate(speed)                 #on limite la vitesse d execution de la boucle pour voir
        for i in range(n):          #l animation (le CPU est trop rapide)
            corps = Corps[i]
            MAJvitesse(corps, M[i])
            MAJposition(corps)

nbody(Corps)
