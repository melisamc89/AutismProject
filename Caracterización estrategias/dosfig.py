import math
import numpy
import os
from scipy import stats
import numpy as np
from funciones_generales import *
from pereza import *

def t_chi2_dosfig(directorio1,directorio2,name,cant,edad,sexo,pob,alfa,media,variable):

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

    if variable==0:
        file = open(os.path.join('.',directorio2,'chi2_dosfig.txt'),'a')
        archivo = open(os.path.join('.',directorio2,'aceptados_dosfig.txt'),'a')
    else:
        file = open(os.path.join('.',directorio2,'chi2_dosfig_sin_pereza.txt'),'a')
        archivo = open(os.path.join('.',directorio2,'aceptados_dosfig_sin_pereza.txt'),'a')

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

    for i in range(10):
        var1=0
        for j in range(cant):
            s = respuesta[j,i]-media[i]
            if s > math.pi:
                s = s-2*math.pi
            else:
                if s< -math.pi:
                    s = s+2*math.pi
            auxiliar.append(s)
            var1=numpy.var(auxiliar)*cant/(cant-1)
        error_nuevo.append(var1)
    var1_prom = numpy.mean(error_nuevo)
    var_prom = math.sqrt(var1_prom)
    
    chi2=0
    m=0
    
    c0 = pow((media[0]-3*math.pi/4)/var_prom,2)
    c1 = pow((media[1]-2*math.pi/4)/var_prom,2)
    c2 = pow((media[2]-6*math.pi/4)/var_prom,2)
    c3 = pow((media[3]-2*math.pi/4)/var_prom,2)
    c4 = pow((media[4]-5*math.pi/4)/var_prom,2)
    c5 = pow((media[5]-4*math.pi/4)/var_prom,2)
    c6 = pow((media[6]-5*math.pi/4)/var_prom,2)
    c7 = pow((media[7]-4*math.pi/4)/var_prom,2)
    c8 = pow((media[8]-5*math.pi/4)/var_prom,2)
    c9 = pow((media[9]-2*math.pi/4)/var_prom,2)

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

