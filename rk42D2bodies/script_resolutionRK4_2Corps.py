# résolution numétique RK 4 avec scipy première et deuxième situation (2 corps )

# importation des modules 
from __future__ import division
from scipy import *
from pylab import *
from scipy.integrate import odeint    

# déclaration des constantes
M1=2*10**30
M2=1.3*2*10**30
G=6.674*10**-11

# fonction scipy
def deriv(syst, t):
    [x1,y1,x2,y2,vx1,vy1,vx2,vy2] = syst               
    
    dx1dt=vx1                                           
    dy1dt=vy1                                         
    dx2dt=vx2                                           
    dy2dt=vy2                                             
    dvx1dt=G*M2*(x2-x1)/sqrt((x1-x2)**2+(y1-y2)**2)**3
    dvy1dt=G*M2*(y2-y1)/sqrt((x1-x2)**2+(y1-y2)**2)**3 
    dvx2dt=G*M1*(x1-x2)/sqrt((x1-x2)**2+(y1-y2)**2)**3  
    dvy2dt=G*M1*(y1-y2)/sqrt((x1-x2)**2+(y1-y2)**2)**3  
    return [dx1dt, dy1dt, dx2dt, dy2dt,  dvx1dt, dvy1dt, dvx2dt, dvy2dt]        

# Paramètres d'intégration
start = 0
end = 1500
numsteps = 100000
t = linspace(start,end,numsteps)

# conditions initiales
x10, y10 = -1.5*10**8, 0   
vx10, vy10 = 0, 9*10**4
x20, y20 = 1.5*10**8, 0
vx20, vy20 = 0, -9*10**4
syst_CI=array([x10, y10, x20, y20,  vx10, vy10, vx20, vy20])   

# Résolution numérique des équations différentielles
Sols=odeint(deriv,syst_CI,t)            
[x1,y1,x2,y2,vx1,vy1,vx2,vy2] = Sols . T  

# Abscisse et ordonée du barycentre
xG = (M1*x1+M2*x2)/(M1+M2)                    
yG = (M1*y1+M2*y2)/(M1+M2)  


# Graphiques des solutions      
plot(x1, y1, 'o', ms=6, mfc='w', mec='b', label=u"M1")  
plot(x2, y2, 'o', ms=6, mfc='w', mec='r', label=u"M2")
plot(xG, yG, '+', ms=6, mfc='w', mec='k', label=u"G")
ylabel('y (m)') 
xlabel('x(m)')
         
axis('equal')
legend()
show()