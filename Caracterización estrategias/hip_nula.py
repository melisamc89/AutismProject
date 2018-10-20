import math
import numpy
import os
from scipy import stats
import numpy as np
from pereza import *

def t_chi2(directorio1,directorio2,name,cant,edad,sexo,pob,alfa,media):
    
    sums = numpy.array([])
    error = numpy.array([])

    for i in range(cant):
        path = os.path.join('.',directorio1,name + str(i + 1) + '.txt') 
        col1,col2 = numpy.loadtxt(path,skiprows=1,usecols=(0,1),dtype=float,unpack=True)
        presentado = col1
        error_col = col2
        error = numpy.concatenate((error, error_col))
    
    file = open(os.path.join('.',directorio2,'chi2_prom.txt'),'a')
    archivo = open(os.path.join('.',directorio2,'aceptados_H0.txt'),'a')

    personales = [name,str(cant),str(edad),sexo,pob]
    for elemento in personales:
        file.write(elemento)
        file.write("\t")

    map = lambda f, data: numpy.vectorize(f)(data)
    
    media_total = numpy.mean(error)
    var1 = (numpy.var(error)*cant*10/(cant*10-1))/cant
    var_total = math.sqrt(var1)

    error.shape = (-1,10)
    
    media = numpy.mean(error,axis=0)
    var2 = (numpy.var(error,axis=0)*cant/(cant-1))/cant
    
    var_prom2 = numpy.mean(var2)
    var_prom = math.sqrt(var_prom2)

    chi2=0
    
    for i in range(10):
        chi2 = chi2 + pow(media[i]/var_prom,2)
    #print(str(chi2))
    pvalue= 1-stats.chi2.cdf(chi2,10)
    file.write(str(pvalue))
    file.write("\n")
    
    if (pvalue > alfa ):
        
        for elemento in personales:
            archivo.write(elemento)
            archivo.write("\t")
        archivo.write(str(pvalue))
        archivo.write("\n")

        return 1
    else:
        return 0

    file.write("\n")
    file.close()
    archivo.write("\n")
    archivo.close()


def t_chi2_pereza(directorio1,directorio2,name,cant,edad,sexo,pob,alfa,media):

    pereza,b = fpereza(name,cant)
    
    sums = numpy.array([])
    error = numpy.array([])

    direc = os.path.join('.','datos',name+str(1)+'.txt')
    presentado = numpy.loadtxt(direc,skiprows=1,usecols=(0,),dtype=int,unpack=True)

    for i in range(cant):
        path = os.path.join('.',directorio1,name + str(i + 1) + '.txt') 
        col1,col2 = numpy.loadtxt(path,skiprows=1,usecols=(0,1),dtype=int,unpack=True)
        error_col  = col2-(pereza*col1)-b
        error = numpy.concatenate((error, error_col))
    
    file = open(os.path.join('.',directorio2,'chi2_pereza.txt'),'a')
    archivo = open(os.path.join('.',directorio2,'aceptados_H0 con pereza.txt'),'a')

    personales = [name,str(cant),str(edad),sexo,pob]
    for elemento in personales:
        file.write(elemento)
        file.write("\t")

    map = lambda f, data: numpy.vectorize(f)(data)
    
    media_total = numpy.mean(error)
    var1 = (numpy.var(error)*cant*10/(cant*10-1))/cant
    var_total = math.sqrt(var1)
    
    error.shape = (-1,10)
    
    media = numpy.mean(error,axis=0)
    var2 = (numpy.var(error,axis=0)*cant/(cant-1))/cant
        
    var_prom2 = numpy.mean(var2)
    var_prom = math.sqrt(var_prom2)

    chi2=0
    m=0
    for i in range(10):
        x=presentado[i]
        chi2 = chi2 + pow((media[i]/var_total),2)
    #print(str(chi2))
    pvalue= 1-stats.chi2.cdf(chi2,8)
    file.write(str(pvalue))
    file.write("\n")
    
    if (pvalue > alfa ):
        for elemento in personales:
            archivo.write(elemento)
            archivo.write("\t")
        archivo.write(str(pvalue))
        archivo.write("\n")
        return 1
    else:
        return 0

    file.write("\n")
    file.close()
    archivo.write("\n")
    archivo.close()
