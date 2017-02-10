from visual import *
import numpy as np
from math import *
from scipy import *
from pylab import *
from scipy.integrate import odeint   
import matplotlib.pyplot as plt
import wx
import os
import sys
from visual import *
import thread
import numpy as np
from visual.graph import *


mA=1     #masse du corps A
mB=1     #masse du corps B
mC=0.001 #masse du corps C (le vaisseau spatial)
G=1      #constante gravitationelle


def deriv(U, t):
    """9 équations d'ordre 2 que l'on réécrit en un système de 18 équations du premier ordre
    cette fonction est la fonction que l'on met en argument du module odeint de scipy"""
    global G,mA,mB,mC
    [xA,yA,zA,xB,yB,zB,xC,yC,zC,vxA,vyA,vzA,vxB,vyB,vzB,vxC,vyC,vzC] = U     #Variables  ; U = vecteur d'état
    dAB=sqrt((xA-xB)**2+(yA-yB)**2+(zA-zB)**2)**3     #precalcul des distances
    dBC=sqrt((xB-xC)**2+(yC-yB)**2+(zC-zB)**2)**3     #precalcul des distances
    dAC=sqrt((xA-xC)**2+(yA-yC)**2+(zA-zC)**2)**3     #precalcul des distances
    dxA=vxA                                           
    dyA=vyA
    dzA=vzA                                           
    dxB=vxB                                           
    dyB=vyB
    dzB=vzB   
    dxC=vxC
    dyC=vyC 
    dzC=vzC                                          
    dvxA=-G*(xA-xB)*mB/dAB -G*(xA-xC)*mC/dAC 
    dvyA=-G*(yA-yB)*mB/dAB -G*(yA-yC)*mC/dAC 
    dvzA=-G*(zA-zB)*mB/dAB -G*(zA-zC)*mC/dAC 
    dvxB=G*(xA-xB)*mA/dAB  -G*(xB-xC)*mC/dBC 
    dvyB=G*(yA-yB)*mA/dAB  -G*(yB-yC)*mC/dBC 
    dvzB=G*(zA-zB)*mA/dAB  -G*(zB-zC)*mC/dBC 
    dvxC=-G*(xC-xB)*mB/dBC -G*(xC-xA)*mA/dAC 
    dvyC=-G*(yC-yB)*mB/dBC -G*(yC-yA)*mA/dAC
    dvzC=-G*(zC-zB)*mB/dBC -G*(zC-zA)*mA/dAC
    return [dxA, dyA, dzA, dxB, dyB, dzB, dxC, dyC, dzC, dvxA, dvyA, dvzA, dvxB, dvyB, dvzB, dvxC, dvyC, dvzC]# Dérivées des variables    
    
def ENmeca(U):
    '''fonction qui prend en argument le vecteur d'état U
    et qui renvoit l'énergie mécanique du système à l'instant correspondant'''
    global mA,mB,mC,G
    [xA,yA,zA,xB,yB,zB,xC,yC,zC,vxA,vyA,vzA,vxB,vyB,vzB,vxC,vyC,vzC] = U 
    E = 0
    E += 0.5*mA*(vxA**2+vyA**2+vzA**2)  #énergie cinétique de A
    E += 0.5*mB*(vxB**2+vyB**2+vzB**2)  #énergie cinétique de B
    E += 0.5*mC*(vxC**2+vyC**2+vzC**2)  #énergie cinétique de C
    E -= G * mA * mB / sqrt((xB-xA)**2+(yB-yA)**2+(zB-zA)**2) #énergie potentielle gravitationelle entre A et B
    E -= G * mA * mC / sqrt((xC-xA)**2+(yC-yA)**2+(zC-zA)**2) #énergie potentielle gravitationelle entre A et C
    E -= G * mC * mB / sqrt((xC-xB)**2+(yC-yB)**2+(zC-zB)**2) #énergie potentielle gravitationelle entre B et C
    return E

def maketrail(Corps1,Corps2,Corps3,t):
    '''fonction qui permet de d'afficher la trajectoire des corps sur une durée déterminée
    ce qui augmente la   visibilité des trajectoires'''
    global dt,ti
    if t == ti + dt:
        Corps1.make_trail = True
        Corps1.trail_type = "curve"
        Corps2.make_trail = True
        Corps2.trail_type = "curve"
        Corps3.make_trail = True
        Corps3.trail_type = "curve"
        
        
###initialisation des parametres###
ti = 0                #instant initial
tf = 80               #instant final
n = 10000             #nombre d'itérations
t = linspace(ti,tf,n) #creation d un vecteur temps, de pas (tf-ti)/n
dt=(tf-ti)/n          #pas de temps
speed=100             #vitesse d'animation, nombre d'iteration par seconde (argument de la fonction rate)

scene.scale=(0.1,0.1,0.1) #zoom initial sur la scene
scene.title = "3 corps"   #titre de la fenetre d'animation
scene.fov = pi / 2        #angle de vue sur la scene
####################################

###Conditions initiales###
xA0, yA0, zA0 = 1, 0, 0
vxA0, vyA0, vzA0 = 0, 0.2, 0
xB0, yB0, zB0 = -1, 0, 0
vxB0, vyB0, vzB0 = 0, -0.2, 0
xC0, yC0, zC0 = 0, 0, 0
vxC0, vyC0, vzC0 = 0, 0, 1.6
U0=array([xA0,yA0,zA0,xB0,yB0,zB0,xC0,yC0,zC0,vxA0,vyA0,vzA0,vxB0,vyB0,vzB0,vxC0,vyC0,vzC0])  #vecteur d'état à l'instant initial
##########################

###Resolution###
Sols=odeint(deriv,U0,t)           
################

###AFFICHAGE####
rayon = 0.05


corps0 = sphere(radius=rayon, make_trail=False, color=color.cyan,retain=2100) #retain = nombre d'iterations prises en compte pour maketrail
corps1 = sphere(radius=rayon, make_trail=False, color=color.white,retain=2100)
corps2 = sphere(radius=rayon, make_trail=False, color=color.red,retain=100)
corps0.m = mA
corps1.m = mB
corps2.m = mC

###vitesses
corps0.v = vector(vxA0, vyA0, vzA0)
corps1.v = vector(vxB0, vyB0, vzB0)
corps2.v = vector(vxC0, vyC0, vzC0)
###positions
corps0.x, corps0.y, corps0.z = xA0, yA0, zA0
corps1.x, corps1.y, corps1.z = xB0, yB0, zB0
corps2.x, corps2.y, corps2.z = xC0, yC0, zC0


def nbody(Corps0,Corps1,Corps2,M):
    '''fonction principale qui effectue les iterations et met a jour les vitesses/positions'''
    global n,ti,dt,tf
    t=ti  #même si c'est une boucle for, on définit une variable t pour la fonction maketrail
    for i in range(n):
        maketrail(Corps0,Corps1,Corps2,t)
        rate(speed)      # vitesse de l'animation déterminée par speed définie plus haut
        Corps0.v = vector(M[i,9], M[i,10], M[i,11])
        Corps0.pos = vector(M[i,0], M[i,1], M[i,2])
        Corps1.v = vector(M[i,12], M[i,13], M[i,14])
        Corps1.pos = vector(M[i,3], M[i,4], M[i,5])
        Corps2.v = vector(M[i,15], M[i,16], M[i,17])
        Corps2.pos = vector(M[i,6], M[i,7], M[i,8])
        t+=dt
        
###graph d'énergie###       
E=[]
for i in range(n):
    E.append(ENmeca(Sols[i,:]))
plt.plot(t,E)
plt.show()
#####################

nbody(corps0,corps1,corps2,Sols)
    


