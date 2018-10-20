import math
import numpy
import os
from test import *
from scipy import stats
import numpy as np

def t_test_total(directorio1,directorio2,name,cant,edad,sexo,pob,alfa,media):
    
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

    file1 = open(os.path.join('.',directorio2,'t-test-total.txt'),'a')
    
    personales = [name,str(cant),str(edad),sexo,pob]
    
    for elemento in personales:
        file1.write(elemento)
        file1.write("\t")
    
    #file1.write (str(tstatistic))
    #file1.write("\t")
    file1.write (str(pvalue))
    file1.write("\t")

    if pvalue < alfa:
        file1.write("0")
        file1.write("\n")
        #print('total:')
        #print(name)
        #print('\n')
        #print(pob)
        #print('\n')
        return 0
    else:
        file1.write ("1")
        file1.write("\n")
        return 1
    
    file1.write("\n")
    file1.close()

def t_test_angulos(directorio1,directorio2,name,cant,edad,sexo,pob,alfa,media):

    
    sums = numpy.array([])
    error = numpy.array([])

    for i in range(cant):
        path = os.path.join('.',directorio1,name + str(i + 1) + '.txt') 
        col1,col2 = numpy.loadtxt(path,skiprows=1,usecols=(0,1),dtype=float,unpack=True)
        error_col = col2
        error = numpy.concatenate((error, error_col))
    
    file2 = open(os.path.join('.',directorio2,'t-test-angulos(0-1).txt'),'a')

    personales = [name,str(cant),str(edad),sexo,pob]
    for elemento in personales:
        file2.write(elemento)
        file2.write("\t")
    
    error.shape = (10,-1)
    #print(error)
    #print('\n')

    n=0
    x=1
    
    for i in range (10):
        
        parte = []
        for j in range (cant):
            parte.append(error[i,j])
        #print(parte)
            
        ttest = stats.ttest_1samp(parte,media)
        tstatistic = ttest[0]
        pvalue = ttest[1]
        alfa_ind = 1 - pow((1-alfa),1/10)
        if pvalue > alfa_ind:
            file2.write(str(pvalue))
            file2.write("\t")
            n=n+1
        else:
            file2.write (str(pvalue))
            file2.write("\t")
            #n=n+1
        #x = x*pow((1-pvalue),1/10) ESTO NO TIENE SENTIDO!!!!!

    #file2.write(str(x))
    #file2.write("\t")
    file2.write(str(n))
    file2.write("\n")
    #if n!=10:
        #print('ind:')
        #print(name)
        #print('\n')
        #print(pob)
        #print('\n')
    file2.close()
    
    return n

def t_chan1(directorio1,directorio2,name,cant,edad,sexo,pob,alfa,media):
    
    sums = numpy.array([])
    error = numpy.array([])

    for i in range(cant):
        path = os.path.join('.',directorio1,name + str(i + 1) + '.txt') 
        col1,col2 = numpy.loadtxt(path,skiprows=1,usecols=(0,1),dtype=float,unpack=True)
        error_col = col2
        error = numpy.concatenate((error, error_col))
    
    file2 = open(os.path.join('.',directorio2,'chan1.txt'),'a')

    personales = [name,str(cant),str(edad),sexo,pob]
    for elemento in personales:
        file2.write(elemento)
        file2.write("\t")
    
    error.shape = (10,-1)
    media = numpy.mean(error,axis=1)
    var = numpy.var(error,axis=1)*cant/(cant-1)

    
    for i in range (10):
        
        parte = []
        for j in range (cant):
            parte.append(error[i,j])
        #print(parte)
            
        ttest = stats.ttest_1samp(parte,media)
        tstatistic = ttest[0]
        pvalue = ttest[1]
        alfa_ind = 1 - pow((1-alfa),1/10)
        if pvalue > alfa_ind:
            #file2.write("0")
            #file2.write("\t")
            n=n+1
        #else:
            #file2.write ("1")
            #file2.write("\t")
            #n=n+1
        #x = x*pow((1-pvalue),1/10) ESTO NO TIENE SENTIDO POR EL SIGNIFICADO DE E FUERA!

    file2.write(str(x))
    file2.write("\t")
    file2.write(str(n))
    file2.write("\n")
    #if n!=10:
        #print('ind:')
        #print(name)
        #print('\n')
        #print(pob)
        #print('\n')
    file2.close()
    
    return n

def Main():
    
    file = open(os.path.join('.','jugadores.txt'),'r')

    directorio1 = os.path.join('.','datos')
    directorio2 = os.path.join('.','resultados')

    ntot=0
    mtot = 0
    a=0
    b=0
    
    
    for datos in file:
        datos = datos.split()
        #print(datos[0])
        name = datos[0]
        cant = int(datos[4])
        edad = int(datos[1])
        sexo = datos[2]
        pob=datos[3]
        b=t_test_total(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0)
        a=t_test_angulos(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0)
        ntot = ntot+a
        mtot = mtot+b

    print("Cantidad de H(0) aceptadas en test angulares:")
    print(ntot)
    print("\n")
    print("Cantidad de H(0) aceptadas en test total:") 
    print(mtot)
        
    file.close()

    print('Se ve que todo anduvo, TE AMO MI VIDA !')
if __name__ == '__main__':
    Main() #ejecuto el Main

