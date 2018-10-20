import os
import numpy 
from funciones import *
import math

def Main():
    name = input('Ingrese el nombre del jugador : \n')
    cant = int(input('Ingrese la cantidad de archivos \n'))
    
    os.chdir(os.path.join('.', 'datos'))
    
    sums = numpy.array([])
    error = numpy.array([])

    direc = name+str(1)+'.txt'
    presentado = numpy.loadtxt(direc,skiprows=1,usecols=(0,),dtype=int,unpack=True)

    for i in range(cant):
        path = name + str(i + 1) + '.txt' 
        col1,col2 = numpy.loadtxt(path,skiprows=1,usecols=(0,1),dtype=int,unpack=True)
        suma_col = col1+col2
        sums = numpy.concatenate((sums,suma_col))
        error = numpy.concatenate((error, col2))    

    sums.shape = (-1,10)
    error.shape = (-1,10)
    
    os.chdir(os.path.join('..', 'resultados'))
    file = open(os.path.join('pereza.txt'),'a')
    
    #prom_respuesta= numpy.mean(sums,axis=0)
    #varianza = numpy.var(sums,axis=0)
    
    prom_error= numpy.mean(error,axis=0)
    varianza_error = numpy.var(error,axis=0)

    recta = numpy.polyfit (presentado,prom_error,1)
    print (recta)
    #return recta[1]
    
    print('Se ve que todo anduvo, TE AMO MI VIDA !')
if __name__ == '__main__':
    Main() #ejecuto el Main
