import math
import numpy
import os
from scipy import stats
import numpy as np
from funciones_generales import *
from pereza import *

def calculo_b(name,cant,directorio1,variable):

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

    a0 = (2*presentado[0]-2*math.pi)*(theta[0]-2*math.pi+presentado[0])
    a1 = (2*presentado[1]-math.pi)*(theta[1]-math.pi+presentado[1])
    a2 = (2*presentado[2]-3*math.pi)*(theta[2]-3*math.pi+presentado[2])
    a3 = (2*presentado[3]-math.pi)*(theta[3]-math.pi+presentado[3])    
    a4 = (2*presentado[4]-3*math.pi)*(theta[4]-3*math.pi+presentado[4])
    a5 = (2*presentado[5]-2*math.pi)*(theta[5]-2*math.pi+presentado[5])
    a6 = (2*presentado[6]-3*math.pi)*(theta[6]-3*math.pi+presentado[6])
    a7 = (2*presentado[7]-2*math.pi)*(theta[7]-2*math.pi+presentado[7])
    a8 = (2*presentado[8]-3*math.pi)*(theta[8]-3*math.pi+presentado[8])
    a9 = (2*presentado[9]-math.pi)*(theta[9]-math.pi+presentado[9])

    b = a0+a1+a2+a3+a4+a5+a6+a7+a8+a9
    return b

def calculo_a():

    presentado = present()
    map = lambda f, data: numpy.vectorize(f)(data)
    pres = map (xatheta,presentado)
    
    a1 = pow(2*pres[0]-math.pi,2)+pow(2*pres[1]-math.pi,2)+pow(2*pres[2]-math.pi,2)
    a2 = pow(2*pres[3]-2*math.pi,2)+pow(2*pres[4]-2*math.pi,2)+pow(2*pres[5]-2*math.pi,2)
    a3 = pow(2*pres[6]-3*math.pi,2)+pow(2*pres[7]-3*math.pi,2)+pow(2*pres[8]-3*math.pi,2)+pow(2*pres[9]-3*math.pi,2)
    a = a1+a2+a3
    return a

def t_chi2_fmayor(directorio1,directorio2,name,cant,edad,sexo,pob,alfa,media):

    sums = numpy.array([])
    error = numpy.array([])

    for i in range(cant):
        path = os.path.join('.',directorio1,name + str(i + 1) + '.txt') 
        col1,col2 = numpy.loadtxt(path,skiprows=1,usecols=(0,1),dtype=float,unpack=True)
        sumas = col1+col2
        error_col = col2
        sums = numpy.concatenate((sums,sumas))
        error = numpy.concatenate((error, error_col))

    file = open(os.path.join('.',directorio2,'chi2_fmayor.txt'),'a')
    archivo = open(os.path.join('.',directorio2,'aceptados_fmayot.txt'),'a')

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

    #for i in range(10):
        #var1=0
        #for j in range(cant):
            #s = respuesta[j,i]-media[i]
            #if s > math.pi:
                #s = s-2*math.pi
            #else:
                #if s< -math.pi:
                    #s = s+2*math.pi
            #auxiliar.append(s)
            #var1=numpy.var(auxiliar)*cant/(cant-1)
        #error_nuevo.append(var1)
    #var1_prom = numpy.mean(error_nuevo)
    #var_prom = math.sqrt(var1_prom)

    chi2=0
    m=0
    
    b = calculo_b(name,cant,directorio1,0)
    a=calculo_a()
    p= b/a
    p2=pow(p,2)
    #print(name)
    #print (str(p))

    var_prom=[]
    var_prom.append((2*angulo[0]-2*math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-3*math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-3*math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-2*math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-3*math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-2*math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-3*math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-math.pi)*(p-p2))
    
    if p>1:
        p=1
    
    c0 = pow((media[0]-p*(2*angulo[0]-2*math.pi)-(2*math.pi-angulo[0]))/var_prom[0],2)
    c1 = pow((media[1]-p*(2*angulo[1]-math.pi)-(math.pi-angulo[1]))/var_prom[1],2)
    c2 = pow((media[2]-p*(2*angulo[2]-3*math.pi)-(3*math.pi-angulo[2]))/var_prom[2],2)
    c3 = pow((media[3]-p*(2*angulo[3]-math.pi)-(math.pi-angulo[3]))/var_prom[3],2)
    c4 = pow((media[4]-p*(2*angulo[4]-3*math.pi)-(3*math.pi-angulo[4]))/var_prom[4],2)
    c5 = pow((media[5]-p*(2*angulo[5]-2*math.pi)-(2*math.pi-angulo[5]))/var_prom[5],2)
    c6 = pow((media[6]-p*(2*angulo[6]-3*math.pi)-(3*math.pi-angulo[6]))/var_prom[6],2)
    c7 = pow((media[7]-p*(2*angulo[7]-2*math.pi)-(2*math.pi-angulo[7]))/var_prom[7],2)
    c8 = pow((media[8]-p*(2*angulo[8]-3*math.pi)-(3*math.pi-angulo[8]))/var_prom[8],2)
    c9 = pow((media[9]-p*(2*angulo[9]-math.pi)-(math.pi-angulo[9]))/var_prom[9],2)

    chi2 = c0+c1+c2+c3+c4+c5+c6+c7+c8+c9
    #print(str(chi2))
    pvalue= 1-stats.chi2.cdf(chi2,9)
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
        print(name)
        return 0

    file.write("\n")
    archivo.write("\n")
    file.close()
    archivo.close()

def t_chi2_fmayor_pereza(directorio1,directorio2,name,cant,edad,sexo,pob,alfa,media):

    pereza,b = fpereza(name,cant)
    
    sums = numpy.array([])
    error = numpy.array([])

    for i in range(cant):
        path = os.path.join('.',directorio1,name + str(i + 1) + '.txt') 
        col1,col2 = numpy.loadtxt(path,skiprows=1,usecols=(0,1),dtype=float,unpack=True)
        sumas = col1+col2-(pereza*col1)-b
        error_col = col2-(pereza*col1)-b
        sums = numpy.concatenate((sums,sumas))
        error = numpy.concatenate((error, error_col))

    file = open(os.path.join('.',directorio2,'chi2_fmayor_pereza.txt'),'a')
    archivo = open(os.path.join('.',directorio2,'aceptados_fmayot_pereza.txt'),'a')

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
    
    chi2=0
    m=0
    
    b = calculo_b(name,cant,directorio1,0)
    a=calculo_a()
    p= b/a
    p2=pow(p,2)
    #print(name)
    #print (str(p))

    var_prom=[]
    var_prom.append((2*angulo[0]-2*math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-3*math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-3*math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-2*math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-3*math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-2*math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-3*math.pi)*(p-p2))
    var_prom.append((2*angulo[0]-math.pi)*(p-p2))
    
    if p>1:
        p=1
    
    c0 = pow((media[0]-p*(2*angulo[0]-2*math.pi)-(2*math.pi-angulo[0]))/var_prom[0],2)
    c1 = pow((media[1]-p*(2*angulo[1]-math.pi)-(math.pi-angulo[1]))/var_prom[1],2)
    c2 = pow((media[2]-p*(2*angulo[2]-3*math.pi)-(3*math.pi-angulo[2]))/var_prom[2],2)
    c3 = pow((media[3]-p*(2*angulo[3]-math.pi)-(math.pi-angulo[3]))/var_prom[3],2)
    c4 = pow((media[4]-p*(2*angulo[4]-3*math.pi)-(3*math.pi-angulo[4]))/var_prom[4],2)
    c5 = pow((media[5]-p*(2*angulo[5]-2*math.pi)-(2*math.pi-angulo[5]))/var_prom[5],2)
    c6 = pow((media[6]-p*(2*angulo[6]-3*math.pi)-(3*math.pi-angulo[6]))/var_prom[6],2)
    c7 = pow((media[7]-p*(2*angulo[7]-2*math.pi)-(2*math.pi-angulo[7]))/var_prom[7],2)
    c8 = pow((media[8]-p*(2*angulo[8]-3*math.pi)-(3*math.pi-angulo[8]))/var_prom[8],2)
    c9 = pow((media[9]-p*(2*angulo[9]-math.pi)-(math.pi-angulo[9]))/var_prom[9],2)

    chi2 = c0+c1+c2+c3+c4+c5+c6+c7+c8+c9
    #print(str(chi2))
    pvalue= 1-stats.chi2.cdf(chi2,9)
    if (pvalue > alfa ):
        file.write(str(pvalue))
        for elemento in personales:
            archivo.write(elemento)
            archivo.write("\t")
        archivo.write(str(pvalue))
        archivo.write("\n")
        file.write("\n")
        return 1
    else:
        file.write(str(pvalue))
        file.write("\n")
        return 0

    file.write("\n")
    archivo.write("\n")
    file.close()
    archivo.close()
