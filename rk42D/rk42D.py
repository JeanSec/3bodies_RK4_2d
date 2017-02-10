from __future__ import division
from scipy.integrate import odeint      
from scipy import *
from pylab import *
import matplotlib.pyplot as plt

mA=2    #masse du corps A
mB=1.3  #masse du corps B
mC=0.01 #masse du corps C (le vaisseau spatial)
G=1     #constante gravitationelle

def deriv(U, t):
    """6 équations d'ordre 2 que l'on réécrit en un système de 12 équations du premier ordre
    cette fonction est la fonction que l'on met en argument du module odeint de scipy"""
    global G,mA,mB,mC
    [xA,yA,xB,yB,xC,yC,vxA,vyA,vxB,vyB,vxC,vyC] = U  #Variables  ; U = vecteur d'état
    dAB=sqrt((xA-xB)**2+(yA-yB)**2)**3  #pre calcul des distances pour economiser du temps de calcul   
    dBC=sqrt((xB-xC)**2+(yC-yB)**2)**3  #pre calcul des distances pour economiser du temps de calcul   
    dAC=sqrt((xA-xC)**2+(yA-yC)**2)**3  #pre calcul des distances pour economiser du temps de calcul   
    dxA=vxA                                     #equa diff 1                     
    dyA=vyA                                     #equa diff 2       
    dxB=vxB                                     #equa diff 3       
    dyB=vyB                                     #equa diff 4
    dxC=vxC                                     #equa diff 5 
    dyC=vyC                                     #equa diff 6       
    dvxA=-G*(xA-xB)*mB/dAB -G*(xA-xC)*mC/dAC    #equa diff 7 
    dvyA=-G*(yA-yB)*mB/dAB -G*(yA-yC)*mC/dAC    #equa diff 8 
    dvxB=G*(xA-xB)*mA/dAB -G*(xB-xC)*mC/dBC     #equa diff 9 
    dvyB=G*(yA-yB)*mA/dAB  -G*(yB-yC)*mC/dBC    #equa diff 10 
    dvxC=-G*(xC-xB)*mB/dBC -G*(xC-xA)*mA/dAC    #equa diff 11 
    dvyC=-G*(yC-yB)*mB/dBC  -G*(yC-yA)*mA/dAC   #equa diff 12 
    return [dxA, dyA, dxB, dyB, dxC, dyC, dvxA, dvyA, dvxB, dvyB, dvxC, dvyC]   # Dérivées des variables 

def ENmeca(U):
    '''fonction qui prend en argument le vecteur d'état U
    et qui renvoit l'énergie mécanique du système à l'instant correspondant'''
    global mA,mB,mC,G
    [xA,yA,xB,yB,xC,yC,vxA,vyA,vxB,vyB,vxC,vyC] = U 
    E = 0
    E += 0.5*mA*(vxA**2+vyA**2)  #énergie cinétique de A
    E += 0.5*mB*(vxB**2+vyB**2)  #énergie cinétique de B
    E += 0.5*mC*(vxC**2+vyC**2)  #énergie cinétique de C
    E -= G * mA * mB / sqrt((xB-xA)**2+(yB-yA)**2) #énergie potentielle gravitationelle entre A et B
    E -= G * mA * mC / sqrt((xC-xA)**2+(yC-yA)**2) #énergie potentielle gravitationelle entre A et C
    E -= G * mC * mB / sqrt((xC-xB)**2+(yC-yB)**2) #énergie potentielle gravitationelle entre B et C
    return E
    

    
###initialisation des parametres###
ti = 0                #instant initial
tf = 20               #instant final
n = 100               #nombre d'itérations
t = linspace(ti,tf,n) #creation d un vecteur temps, de pas (tf-ti)/n

#############################Conditions initiales##################################
xA0, yA0 = 1, 0   
vxA0, vyA0 = 0, 0.2
xB0, yB0 = -1, 0
vxB0, vyB0 = 0, -0.2
xC0, yC0 = -1, 1.5
vxC0, vyC0 = -1, 0.5
U0=array([xA0,yA0,xB0,yB0,xC0,yC0,vxA0,vyA0,vxB0,vyB0,vxC0,vyC0])  #vecteur u0 avec conditions initiales
###################################################################################


Sols=odeint(deriv,U0,t)           #récupération des solution sous forme d'une matrice
                                  #chaque ligne représente le vecteur U à différents instants
                                  #Sols est donc de taille n*12
[xA,yA,xB,yB,xC,yC,vxA,vyA,vxB,vyB,vxC,vyC] = Sols . T        
xG = (mA*xA+mB*xB)/(mA+mB)                      # Abscisse du barycentre (corps C négligé)
yG = (mA*yA+mB*yB)/(mA+mB)                      # Ordonnée du barycentre

     
###Validation des résultats par conservation de l'énergie mécanique###
Ei = ENmeca(U0)  #énergie mécanique initiale
Uf = Sols[n-1,:] #énergie mécanique finale
Ef = ENmeca(Uf)  #différence d'énergie entre le début et la fin de la simulation
print (Ei-Ef)
###creation d une liste pour suivre l'énergie au cours de la simulation
E=[]
for i in range(n):
    E.append(ENmeca(Sols[i,:]))
######################################################################


###Affichage###
plt.figure(1)
plt.plot(xA, yA, 'o', ms=3, mec='b', label=u"A")   
plt.plot(xB, yB, 'o', ms=3, mec='r', label=u"B")   
plt.plot(xC, yC, 'o', ms=3, mec='w', label=u"C")   
plt.plot(xG, yG, 'o', ms=3, mfc='w', mec='k', label=u"G")  
axis('equal')
legend()
#creation d une deuxieme figure pour afficher le graphique de l'énergie 
#mécanique du système en fonction du temps
plt.figure(2)
plt.plot(t,E)
plt.title("Energie mecanique en fonction du temps")
plt.xlabel("t(s)")
plt.ylabel("E(J)")
show()
