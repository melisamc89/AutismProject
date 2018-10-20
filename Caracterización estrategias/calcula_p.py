import random
import math
import numpy
import os
from scipy import stats
import numpy as np
from pereza import *

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
    
def Main():

    file = open(os.path.join('.','jugadores.txt'),'r')
    
    directorio1 = os.path.join('.','datos')
    directorio2 = os.path.join('.','resultados')

    archivo = open(os.path.join('.',directorio2,'probabilidad_sujeto.txt'),'a')
    
    a = calculo_a()
    
    for datos in file:
        datos = datos.split()
        name = datos[0]
        cant = int(datos[4])
        edad = int(datos[1])
        sexo = datos[2]
        pob=datos[3]
        b = calculo_b(name,cant,directorio1,0)
        p = b/a
        personales = [name,str(cant),str(edad),sexo,str(pob)]
        for elemento in personales:
            archivo.write(elemento)
            archivo.write("\t")
        archivo.write(str(p))
        archivo.write("\n")
        #print (name)
        print(p)
    
    file.close()

    #print('Se ve que todo anduvo, TE AMO MI VIDA !')

if __name__ == '__main__':
    Main() #ejecuto el Main
