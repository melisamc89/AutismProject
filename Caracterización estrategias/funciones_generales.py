import math
import numpy
import os
from scipy import stats
import numpy as np

def xatheta(v):
    return (2*math.pi*((v - 412)/ (857 - 412)))

def erroratheta(v):
    return (2*math.pi*(v/ (857 - 412)))

def thetaax(v):
    return (412+((857-412)*v/(2*math.pi)))

def creador_theta(array1,array2):
    theta =[]
    for i in range (10):
        if array1[i] < 0:
            theta1= numpy.arctan(array2[i]/array1[i])+math.pi
        else:
            if array2 [i] > 0:
                theta1= numpy.arctan(array2[i]/array1[i])
            else:
                theta1= numpy.arctan(array2[i]/array1[i])+2*math.pi
        theta.append(theta1)
    return theta

def present():
    
    path = os.path.join('.','presentados.txt') #direccion archivo con angulos presentados
    file = open(path,'r')
    col1 = numpy.loadtxt(path,dtype=int,unpack=True)#guardo la primer columna en col1
    #print(col1)
    file.close()
    #print(col1)
    return col1 # la función devuelve col1
