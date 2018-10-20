import math
import numpy
import os
from scipy import stats
import numpy as np
from hip_nula import *
from fig_mayor import *
from fig_menor import *
from fig_estrella import *
from fig_cuadrado import *
from fig_circulo import *
from fig_triangulo import *
from dosfig import*

def Main():
    
    file = open(os.path.join('.','jugadores.txt'),'r')

    directorio1 = os.path.join('.','datos')
    directorio2 = os.path.join('.','resultados')
    
    H0=0
    H0_p=0
    FM=0
    FM_p=0
    FMenor=0
    FMenor_p=0
    Fig_est=0
    Fig_est_p=0
    Fig_cua=0
    Fig_cua_p=0
    Fig_cir=0
    Fig_cir_p=0
    Fig_tri=0
    Fig_tri_p=0
    dosfig=0
    dosfig_p=0
    
    for datos in file:
        datos = datos.split()
        #print(datos[0])
        name = datos[0]
        cant = int(datos[4])
        edad = int(datos[1])
        sexo = datos[2]
        pob=datos[3]
        #H0_ind = t_chi2(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0)
        #H0_p_ind = t_chi2_pereza(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0)
        #FM_ind = t_chi2_fmayor(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0)
        #FM_ind_p = t_chi2_fmayor_pereza(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0)
        FMenor_ind = t_chi2_fmenor(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0)
        FMenor_ind_p = t_chi2_fmenor_pereza(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0)
        #Fig_est_ind= t_chi2_estrella(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0,0)
        #Fig_est_ind_p= t_chi2_estrella(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0,1)
        #Fig_cua_ind= t_chi2_cuadrado(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0,0)
        #Fig_cua_ind_p= t_chi2_cuadrado(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0,1)
        #Fig_cir_ind= t_chi2_circulo(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0,0)
        #Fig_cir_ind_p= t_chi2_circulo(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0,1)
        #Fig_tri_ind= t_chi2_triangulo(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0,0)
        #Fig_tri_ind_p= t_chi2_triangulo(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0,1)
        #dosfig_ind = t_chi2_dosfig(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0,0)
        #dosfig_ind_p = t_chi2_dosfig(directorio1,directorio2,name,cant,edad,sexo,pob,0.05,0,1)


        #H0 = H0 + H0_ind
        #H0_p = H0_p + H0_p_ind
        #FM = FM + FM_ind
        #FM_p = FM_p + FM_ind_p
        FMenor = FMenor + FMenor_ind
        FMenor_p = FMenor_p + FMenor_ind_p
        #Fig_est = Fig_est + Fig_est_ind
        #Fig_est_p = Fig_est_p + Fig_est_ind_p
        #Fig_cua = Fig_cua + Fig_cua_ind
        #Fig_cua_p = Fig_cua_p + Fig_cua_ind_p
        #Fig_cir = Fig_cir + Fig_cir_ind
        #Fig_cir_p = Fig_cir_p + Fig_cir_ind_p
        #Fig_tri = Fig_tri + Fig_tri_ind
        #Fig_tri_p = Fig_tri_p + Fig_tri_ind_p
        #dosfig = dosfig + dosfig_ind
        #dosfig_p = dosfig_p + dosfig_ind_p

    #print("Sin restar pereza:")
    #print(H0)
    #print("restando pereza:")
    #print(H0_p)
    #print("Estrategia figura mayor:")
    #print(FM)
    #print("Estrategia figura mayor_pereza:")
    #print(FM_p)
    print("Estrategia figura menor:")
    print(FMenor)
    print("Estrategia figura menor_pereza:")
    print(FMenor_p)
    #print("Estrategia figura estrella:")
    #print(Fig_est)
    #print("Estrategia figura estrella_pereza:")
    #print(Fig_est_p)
    #print("Estrategia figura cuadrado:")
    #print(Fig_cua)
    #print("Estrategia figura cuadrado_pereza:")
    #print(Fig_cua_p)
    #print("Estrategia figura circulo:")
    #print(Fig_cir)
    #print("Estrategia figura circulo_pereza:")
    #print(Fig_cir_p)
    #print("Estrategia figura triangulo:")
    #print(Fig_tri)
    #print("Estrategia figura triangulo_pereza:")
    #print(Fig_tri_p)
    #print("Estrategia dos fig:")
    #print(dosfig)
    #print("Estrategia dosfig_p:")
    #print(dosfig_p)
    
    file.close()

    #print('Se ve que todo anduvo, TE AMO MI VIDA !')
if __name__ == '__main__':
    Main() #ejecuto el Main
