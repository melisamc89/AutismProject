import math
import numpy
import os
from scipy import stats
import numpy as np

def fpereza (name,cant):
    
    sums = numpy.array([])
    error = numpy.array([])

    direc = os.path.join('.','datos',name+str(1)+'.txt')
    presentado = numpy.loadtxt(direc,skiprows=1,usecols=(0,),dtype=int,unpack=True)

    for i in range(cant):
        path = os.path.join('.','datos', name + str(i + 1) + '.txt') 
        col1,col2 = numpy.loadtxt(path,skiprows=1,usecols=(0,1),dtype=int,unpack=True)
        error = numpy.concatenate((error, col2))    

    sums.shape = (-1,10)
    error.shape = (-1,10)

    prom_error= numpy.mean(error,axis=0)

    recta = numpy.polyfit(presentado,prom_error,1)
    
    return recta

