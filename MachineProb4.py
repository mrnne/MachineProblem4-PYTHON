# MACHINE PROBLEM 4
# Python Program for solving the Projectile Motion

# importing matplotlib.pyplot, numpy, math, sys

import matplotlib.pyplot as plot
import numpy as np
import math
import sys

# Obtaining inputs
height = float(input('Enter the initial height of Projectile above the ground (m): '))
velocity = float(input('Enter the  magnitude of velocity(m/s): '))
angle = float(input('Enter the angle with respect to the +axis at which the projectile is fired (degrees): '))
axaxis = float(input('Enter the x-component of acceleration (m/s^2): '))
ayaxis= float(input('Enter the y-component of acceleration (m/s^2): '))

ANGLE= angle*(math.pi/180)

# Vertical acceleration cannot be zero, because there would no free fall
if ayaxis == 0: 
    sys.exit('Error! Vertical Acceleration cannot be zero')
    
# Solving for the distance     
distance = np.sqrt((velocity*np.sin(ANGLE))**2 - 4*(1/2*ayaxis)*height) 
       
# Solving for the final time
tmax = (-velocity*np.sin(ANGLE)+distance)/ayaxis
    

# Solving for the time
time= np.linspace(0,tmax) 
    
if tmax <= 0:
    tmax = (-velocity*np.sin(ANGLE)-distance)/ayaxis
    
# Solving for the time
time= np.linspace(0,tmax)
    
# Solving for the Non-Ideal x values
x = velocity*np.cos(ANGLE)*(time) + (1/2)*(axaxis)*(time)**2

# Solving for the Ideal x values
xIdeal= velocity*np.cos(ANGLE)*time 

# Solving for the Non-Ideal y values
y = height+velocity*np.sin(ANGLE)*(time) + (1/2)*(ayaxis)*(time)**2 

# Plotting the Projectile
plot.title('Projectile Motion')
plot.xlabel('Range')
plot.ylabel('Height')
plot.plot(xIdeal,y,'--r', label="Ideal Motion")
plot.plot(x,y,'-k',label="Non-Ideal Motion")
plot.legend(loc="upper right")
plot.grid()
plot.show()