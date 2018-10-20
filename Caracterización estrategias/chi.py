import math
import numpy
import os
from scipy import stats
import numpy as np

def f(x):
    f=0
    return f

def t_chi2(directorio1,directorio2,name,cant,edad,sexo,pob,alfa,media):
    
    sums = numpy.array([])
    error = numpy.array([])

    for i in range(cant):
        path = os.path.join('.',directorio1,name + str(i + 1) + '.txt') 
        col1,col2 = numpy.loadtxt(path,skiprows=1,usecols=(0,1),dtype=float,unpack=True)
        presentado = col1
        error_col = col2
        error = numpy.concatenate((error, error_col))
    
    file = open(os.path.join('.',directorio2,'chi2.txt'),'a')

    personales = [name,str(cant),str(edad),sexo,pob]
    for elemento in personales:
        file.write(elemento)
        file.write("\t")

    map = lambda f, data: numpy.vectorize(f)(data)
    
    media_total = numpy.mean(error)
    #print(media_total)
    var1 = numpy.var(error)
    var_total = math.sqrt(var1)
    #print (var_total)
    
    error.shape = (10,-1)
    
    media = numpy.mean(error,axis=1)
    #print(media)
    var2 = numpy.var(error,axis=1)
    var = map (math.sqrt,var2)
    #print(var)
    var_prom = numpy.mean(var)
    #print(var_prom)


    chi_o=0
    n=0
    for i in range(10):
        chi2_o = chi_o + pow(((media[i]-f(presentado[i]))/var[i]),2)
    #print(chi2_o)
    pvalue_original = stats.chi2.cdf(chi2_o,10)
    #print(pvalue_original)
    if (pvalue_original < alfa ):
        file.write("1")
        n=n+1
    else:
        file.write("0")
        print('original:')
        print(name)
        print('\n')
    #file.write(str(pvalue_original))
    file.write("\t")


    chi2_1=0
    m=0
    for i in range(10):
        chi2_1 = chi2_1 + pow(((media[i]-f(presentado[i]))/var_total),2)
    #print(chi2_1)
    pvalue_c1 = stats.chi2.cdf(chi2_1,10)
    #print(pvalue_c1)
    if (pvalue_c1 < alfa ):
        file.write("1")
        m=m+1
    else:
        file.write("0")
        print('c1')
        print(name)
        print('\n')
    #file.write(str(pvalue_original))
    file.write("\t")


    chi2_2 = 0
    l=0
    for i in range (10):
        chi2_2 = chi2_2 + pow(((media[i]-f(presentado[i]))/var_prom),2)
    #print(chi2_2)
    pvalue_c2 = stats.chi2.cdf(chi2_2,10)
    if (pvalue_c2 < alfa ):
        file.write("1")
        l=l+1
    else:
        file.write("0")
        print('c2')
        print(name)
        print('\n')
    #file.write(str(pvalue_original))
    file.write("\n")

    devuelve = []
    devuelve.append(n)
    devuelve.append(m)
    devuelve.append(l)

    file.close()
    return devuelve

def Main():
    
    file = open(os.path.join('.','jugadores.txt'),'r')

    directorio1 = os.path.join('.','datos')
    directorio2 = os.path.join('.','resultados')

    original=0
    c1=0
    c2=0
    
    for datos in file:
        datos = datos.split()
        #print(datos[0])
        name = datos[0]
        cant = int(datos[4])
        edad = int(datos[1])
        sexo = datos[2]
        pob=datos[3]
        a,b,c = t_chi2(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0)
        original = original + a
        c1 = c1+b
        c2=c2+c

    print (original)
    print(c1)
    print (c2)
    file.close()

    print('Se ve que todo anduvo, TE AMO MI VIDA !')
if __name__ == '__main__':
    Main() #ejecuto el Main

