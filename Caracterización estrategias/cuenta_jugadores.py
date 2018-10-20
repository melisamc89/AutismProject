import math
import numpy
import os

def Main():
    
    file1 = open(os.path.join('.','aceptados_dosfig_sin_pereza.txt'),'r')
    
    espectro = 0
    niños = 0
    jovenes = 0
    adultos = 0
    mayores = 0
    
    for datos in file1:
        datos = datos.split()
        #print(datos[0])
        name = datos[0]
        cant = int(datos[1])
        edad = int(datos[2])
        sexo = datos[3]
        pob=int(datos[4])
        if pob==1:
            espectro = espectro+1
        else:
            if pob==0:
                if edad < 19:
                    niños = niños + 1
                if edad > 18:
                    if edad <35:
                        jovenes = jovenes+1
                if edad > 35:
                    if edad <=45:
                        adultos= adultos+1
                if edad > 45:
                    mayores= mayores+1

    print("Cantidad de sujetos en el espectro:")
    print(str(espectro))
    print("Cantidad de Niños:")
    print(str(niños))
    print("Cantidad de Jovenes:")
    print(str(jovenes))
    print("Cantidad de Adultos:")
    print(str(adultos))
    print("Cantidad de Mayores:")
    print(str(mayores))
    
    file1.close()

    #print('Se ve que todo anduvo, TE AMO MI VIDA !')
if __name__ == '__main__':
    Main() #ejecuto el Main

