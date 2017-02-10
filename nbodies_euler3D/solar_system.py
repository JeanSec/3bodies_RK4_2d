# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 23:28:38 2017

@author: Jean
"""
'''simulation du système solaire à echelle réelle'''

from functions import*
from cond_init import*

##couleurs
colorS=(1, 1, 0.4)
colorM=(0.9, 0.9, 0.9)
colorV =(1, 0.7, 0.2)
colorT =(0.1, 0.4, 0.8)
colorM =(0.9, 0.3, 0.2)
colorJ =(0.8, 0.7, 0.2)
colorS =(1, 0.5, 0.2)
colorU =(0.1, 0.6, 0.8)
colorN =(0.1, 0.4, 0.8)

corps0 = sphere(radius=695700000*10, make_trail=False, color=colorS, retain=1000)
corps1 = sphere(radius=2440000*10, make_trail=False, color=colorM, retain=400)
corps2 = sphere(radius=6052000*10, make_trail=False, color=colorV, retain=1000)
corps3 = sphere(radius=6371000*10, make_trail=False, color=colorT, retain=1700)
corps4 = sphere(radius=3390000*10, make_trail=False, color=colorM, retain=2500)
corps5 = sphere(radius=69911000*10, make_trail=False, color=colorJ, retain=5000)
corps6 = sphere(radius=58232000*10, make_trail=False, color=colorS, retain=6500)
corps7 = sphere(radius=25362000*10, make_trail=False, color=colorU, retain=8000)
corps8 = sphere(radius=24622000*10, make_trail=False, color=colorN, retain=10000)

corps0.m = 1.9891 * 10 ** 30
corps1.m = 330.2 * 10 ** 21
corps2.m = 4.8685 * 10 ** 24
corps3.m = 5.9736 * 10 ** 24
corps4.m = 641.850 * 10 ** 21
corps5.m = 1.8986 * 10 ** 27
corps6.m = 5.683 * 10 ** 26
corps7.m = 8.6810 * 10 ** 25
corps8.m = 102.43 * 10 ** 24

###vitesses
corps0.v = vector(0, 0, 0)
corps1.v = vector(0, 58000.98, 0)
corps2.v = vector(0, -35000.26, 0)
corps3.v = vector(0, 30000.287, 0)
corps4.v = vector(0, -26000.499, 0)
corps5.v = vector(0, 13000.72, 0)
corps6.v = vector(0, -10000.183, 0)
corps7.v = vector(0, 7000.128, 0)
corps8.v = vector(0, -5000.479, 0)

###positions
corps1.x, corps0.y, corps0.z = 0, 0, 0
corps1.x, corps1.y, corps1.z = 46001272000, 0, 0
corps2.x, corps2.y, corps2.z = -107476259000, 0, 0
corps3.x, corps3.y, corps3.z = 147098074000, 0, 0
corps4.x, corps4.y, corps4.z = -206644545000, 0, 0
corps5.x, corps5.y, corps5.z = 740520000000, 0, 0
corps6.x, corps6.y, corps6.z = -1349467375000, 0, 0
corps7.x, corps7.y, corps7.z = 2734998229000, 0, 0
corps8.x, corps8.y, corps8.z = -4452940833000, 0, 0


Corps = [corps0, corps1, corps2, corps3, corps4, corps5, corps6, corps7, corps8]

nbody(Corps,speed2,G0,dt1)