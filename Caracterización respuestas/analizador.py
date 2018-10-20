import os
import numpy 
from funciones1 import *
import math

def Main():
    
    file = open(os.path.join('.','jugadores.txt'),'r')

    for datos in file:
        datos = datos.split()
        print(datos[0],datos[1],datos[2],datos[3],datos[4])
        name = datos[0]
        cant = int(datos[4])
        edad = int(datos[1])
        sexo = datos[2]
        pob=datos[3]
        analisis(name,cant,edad,sexo,pob)
    file.close()

    print('Se ve que todo anduvo, TE AMO MI VIDA !')
if __name__ == '__main__':
    Main() #ejecuto el Main
