# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 23:45:59 2017

@author: Jean
"""

'''problème pythagoricien'''

from functions import*
from cond_init import*

corps0 = sphere(radius=rayon, make_trail=False, color=color.cyan,retain=2**20)
corps1 = sphere(radius=rayon, make_trail=False, color=color.white,retain=2**20)
corps2 = sphere(radius=rayon, make_trail=False, color=color.red,retain=2**20)
corps0.m = 3
corps1.m = 4
corps2.m = 5

###vitesses
corps0.v = vector(0, 0)
corps1.v = vector(0, 0)
corps2.v = vector(0, 0)
###positions
corps0.x, corps0.y, corps0.z = 1, 3, 0
corps1.x, corps1.y, corps1.z = -2, -1, 0
corps2.x, corps2.y, corps2.z = 1, -1, 0

Corps = [corps0, corps1, corps2]

nbody(Corps,speed3,G1,dt2)