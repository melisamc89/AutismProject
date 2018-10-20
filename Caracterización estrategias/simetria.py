import math
import numpy
import os
from test import *
from scipy import stats
import numpy as np

def simetria(directorio1,directorio2,name,cant,edad,sexo,pob,alfa,media):
    
    sums = numpy.array([])
    error = numpy.array([])

    for i in range(cant):
        path = os.path.join('.', directorio1 , name + str(i + 1) + '.txt') 
        col1,col2 = numpy.loadtxt(path,skiprows=1,usecols=(0,1),dtype=float,unpack=True)
        error_col = col2
        error = numpy.concatenate((error, error_col))
        
    ttest = stats.ttest_1samp(error, media)
    tstatistic = ttest[0]
    pvalue = ttest[1]

    file1 = open(os.path.join('.',directorio2,'simetria.txt'),'a')
    
    personales = [name,str(cant),str(edad),sexo,pob]
    
    for elemento in personales:
        file1.write(elemento)
        file1.write("\t")
    

    file1.write (str(pvalue))
    file1.write("\n")

    if pvalue < alfa:
        return 0
    else:
        return 1
    
    file1.write("\n")
    file1.close()

def Main():
    
    file = open(os.path.join('.','jugadores.txt'),'r')

    directorio1 = os.path.join('.','datos')
    directorio2 = os.path.join('.','resultados')

    ntot=0
    a=0
        
    for datos in file:
        datos = datos.split()
        #print(datos[0])
        name = datos[0]
        cant = int(datos[4])
        edad = int(datos[1])
        sexo = datos[2]
        pob=datos[3]
        a=simetria(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0)
        ntot = ntot+a
        
    print("Cantidad de H(0) aceptadas:")
    print(ntot)
    print("\n")
    
    file.close()

    print('Se ve que todo anduvo, TE AMO MI VIDA !')
if __name__ == '__main__':
    Main() #ejecuto el Main

