import math
import numpy
import os
from scipy import stats
import numpy as np
from funciones_generales import *
from pereza import *

def calculo_b_triangulo(name,cant,directorio1,variable):

    pereza,b = fpereza(name,cant)
    
    sums = numpy.array([])
    error = numpy.array([])

    for i in range(cant):
        path = os.path.join('.',directorio1,name + str(i + 1) + '.txt') 
        col1,col2 = numpy.loadtxt(path,skiprows=1,usecols=(0,1),dtype=int,unpack=True)
        if variable==0:
            suma_col = col1+col2
            error_col = col2
        else:
            suma_col = col1+col2-(pereza*col1)-b
            error_col = col2-(pereza*col1)-b
        sums = numpy.concatenate((sums,suma_col))
        error = numpy.concatenate((error, error_col))

    sums.shape = (-1,10)
    error.shape = (-1,10)
    
    map = lambda f, data: numpy.vectorize(f)(data)

    presentado = map(xatheta,col1)
    respuesta = map(xatheta,sums)
    error_rta = map(erroratheta,error)
    
    sin = map(math.sin,respuesta)
    cos = map(math.cos,respuesta)
    e_sin = map (math.sin,error_rta)
    e_cos = map (math.cos, error_rta)
    prom_sin = numpy.mean(sin,axis=0)
    prom_e_sin = numpy.mean(e_sin,axis=0)
    prom_cos = numpy.mean(cos,axis=0)
    prom_e_cos = numpy.mean(e_cos,axis=0)

    theta = creador_theta(prom_cos,prom_sin)

    b=0
    for i in range(10):
        b= b +(2*presentado[i]+math.pi)*(theta[i]+math.pi+presentado[i])
    return b

def calculo_a_triangulo():

    presentado = present()
    map = lambda f, data: numpy.vectorize(f)(data)
    pres = map (xatheta,presentado)

    a=0
    for i in range(10):
        a = a+ pow(2*pres[i]+math.pi,2)
    return a

def t_chi2_triangulo(directorio1,directorio2,name,cant,edad,sexo,pob,alfa,media,variable):

    sums = numpy.array([])
    error = numpy.array([])

    for i in range(cant):
        path = os.path.join('.',directorio1,name + str(i + 1) + '.txt') 
        col1,col2 = numpy.loadtxt(path,skiprows=1,usecols=(0,1),dtype=float,unpack=True)
        if variable==0:
            suma_col = col1+col2
            error_col = col2
        else:
            pereza,b = fpereza(name,cant)
            suma_col = col1+col2-(pereza*col1)-b
            error_col = col2-(pereza*col1)-b
        sums = numpy.concatenate((sums,suma_col))
        error = numpy.concatenate((error, error_col))

    if variable ==0:
        file = open(os.path.join('.',directorio2,'chi2_triangulo.txt'),'a')
        archivo = open(os.path.join('.',directorio2,'aceptados_triangulo.txt'),'a')
    else:
        file = open(os.path.join('.',directorio2,'chi2_triangulo_pereza.txt'),'a')
        archivo = open(os.path.join('.',directorio2,'aceptados_triangulo_pereza.txt'),'a')

    personales = [name,str(cant),str(edad),sexo,pob]
    for elemento in personales:
        file.write(elemento)
        file.write("\t")

    map = lambda f, data: numpy.vectorize(f)(data)

    sums.shape = (-1,10)
    error.shape = (-1,10)

    angulo = map(xatheta,col1)
    respuesta = map(xatheta,sums)
    error_rta = map(erroratheta,error)
    
    sin = map(math.sin,respuesta)
    cos = map(math.cos,respuesta)
    e_sin = map (math.sin,error_rta)
    e_cos = map (math.cos, error_rta)
    
    prom_sin = numpy.mean(sin,axis=0)
    prom_e_sin = numpy.mean(e_sin,axis=0)
    prom_cos = numpy.mean(cos,axis=0)
    prom_e_cos = numpy.mean(e_cos,axis=0)

    media = creador_theta(prom_cos,prom_sin)

    error_nuevo=[]
    auxiliar = []

    var_prom =[]
    for i in range (10):
        var_prom.append(angulo[i])
        
    chi2=0
    m=0
    
    b = calculo_b_triangulo(name,cant,directorio1,variable)
    a = calculo_a_triangulo()
    p= b/a
    #print(name)
    #print (str(p))
    
    if p>1:
        p=1
    chi2=0
    
    for i in range(10):
        chi2 = chi2 + pow((media[i]-p*(2*angulo[i]-2*math.pi)-(2*math.pi-angulo[i]))/var_prom[i],2)
    #print(str(chi2))
    pvalue= 1-stats.chi2.cdf(chi2,9)
    file.write(str(pvalue))
    file.write("\n")
    if (pvalue > alfa ):
        #print(name)
        for elemento in personales:
            archivo.write(elemento)
            archivo.write("\t")
        archivo.write(str(pvalue))
        archivo.write("\n")
        return 1
    else:
        print(name)
        return 0

    file.write("\n")
    archivo.write("\n")
    file.close()
    archivo.close()

