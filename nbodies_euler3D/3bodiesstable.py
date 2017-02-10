# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 22:57:34 2017

@author: Jean
"""

'''une solution d'un probleme a 3 corps ou aucun des corps n'est ejectée'''

from functions import*
from cond_init import*

corps0 = sphere(radius=rayon, make_trail=False, color=color.cyan,retain=2100)
corps1 = sphere(radius=rayon, make_trail=False, color=color.white,retain=2100)
corps2 = sphere(radius=rayon, make_trail=False, color=color.red,retain=2100)
corps0.m = m
corps1.m = m
corps2.m = m

###vitesses
corps0.v = vector(-0.93240737 / 2, -0.86473146 / 2)
corps1.v = vector(-0.93240737 / 2, -0.86473146 / 2)
corps2.v = vector(0.93240737, 0.86473146, 0)
###positions
corps0.x, corps0.y, corps0.z = -0.97000436, 0.24308753, 0
corps1.x, corps1.y, corps1.z = 0.97000436, -0.24308753, 0
corps2.x, corps2.y, corps2.z = 0, 0, 0

Corps = [corps0, corps1, corps2]
nbody(Corps,speed1,G1,dt0)