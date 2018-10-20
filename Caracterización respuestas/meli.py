import os
import numpy 
from funciones import *
import math

def Main():
    name = input('Ingrese el nombre del jugador : \n')
    cant = int(input('Ingrese la cantidad de archivos \n'))
    edad = int (input ('Ingrese la edad del jugador \n'))
    sexo = input('Ingrese el sexo del jugador : \n')
    juego = input('Ingrese si el jugador es del espectro : \n')
    
    os.chdir(os.path.join('.', 'datos'))

    pereza = fpereza (name,cant)
    
    sums = numpy.array([])
    error = numpy.array([])

    direc = name+str(1)+'.txt'
    presentado = numpy.loadtxt(direc,skiprows=1,usecols=(0,),dtype=int,unpack=True)

    for i in range(cant):
        path = name + str(i + 1) + '.txt' 
        col1,col2 = numpy.loadtxt(path,skiprows=1,usecols=(0,1),dtype=int,unpack=True)
        suma_col = col1+col2+(pereza*col1)
        error_col = col2 + (pereza*col1)
        sums = numpy.concatenate((sums,suma_col))
        error = numpy.concatenate((error, error_col))    

    os.chdir(os.path.join('..', 'resultados sin pereza'))

    file = open(os.path.join('globales sin pereza.txt'),'a')

    sums.shape = (-1,10)
    error.shape = (-1,10)

    map = lambda f, data: numpy.vectorize(f)(data)

    #mapeo de las respuestas y error en pixeles a angulo en radianes
    
    presentado = map(xatheta,col1)
    respuesta = map(xatheta,sums)
    error_rta = map(erroratheta,error)

    #mapeo de la respuesta en radianes a sen y cos y sus correspondientes errores
    
    sin = map(math.sin,respuesta)
    cos = map(math.cos,respuesta)
    e_sin = map (math.sin,error_rta)
    e_cos = map (math.cos, error_rta)

    #escribo en un archivo los anteriores mapeos
    
    #write_matrix_to_file (sums,name+'_sums.txt',col1)
    #write_matrix_to_file (error,name+'_error1.txt',col1)
    #write_matrix_to_file (respuesta,name+'_resp.txt',presentado,traspose=True)
    #write_matrix_to_file (error_rta,name+'_error.txt',presentado,traspose=True)
    #write_matrix_to_file (sin,name+'_sin.txt',presentado)
    #write_matrix_to_file (cos,name+'_cos.txt',presentado)

    #calculo el error total de la persona y el score total
    
    error_total = numpy.array([])
    for i in range (cant):
        error_total = numpy.concatenate ((error_total,error[i]))
    error_total_ang = map (erroratheta,error_total)
    puntaje = []
    for i in range (cant*10):
        puntaje.append(pow(error_total_ang,2))
    prom_errores = numpy.mean(error_total_ang)
    prom_puntaje = numpy.mean (puntaje)
    print(prom_errores)
    print(prom_puntaje)

    #calculo los promedios de sen y cos con sus respectivos errores
    
    y = numpy.array([])
    prom_sin = numpy.mean(sin,axis=0)
    varianza_sin = numpy.var(sin,axis=0)*cant/(cant-1)
    y = numpy.concatenate ((prom_sin,varianza_sin))
    y.shape = (2,10)
    #write_matrix_to_file(y,name+'_prom_sin.txt',presentado,traspose=True)
    e_y = numpy.array([])
    prom_e_sin = numpy.mean(e_sin,axis=0)
    varianza_e_sin = numpy.var(e_sin,axis=0)*cant/(cant-1)
    e_y = numpy.concatenate ((prom_e_sin,varianza_e_sin))
    e_y.shape = (2,10)
    #write_matrix_to_file(e_y,name+'_prom_sin.txt',presentado,traspose=True)

    x = numpy.array([])
    prom_cos = numpy.mean(cos,axis=0)
    varianza_cos = numpy.var(cos,axis=0)*cant/(cant-1)
    x = numpy.concatenate ((prom_cos,varianza_cos))
    x.shape = (2,10)
    #write_matrix_to_file(x,name+'_prom_e_cos.txt',presentado,traspose=True)
    e_x = numpy.array([])
    prom_e_cos = numpy.mean(e_cos,axis=0)
    varianza_e_cos = numpy.var(e_cos,axis=0)*cant/(cant-1)
    e_x = numpy.concatenate ((prom_e_cos,varianza_e_cos))
    e_x.shape = (2,10)
    #write_matrix_to_file(e_y,name+'_prom_e_sin.txt',presentado,traspose=True)

    #prom = numpy.array([])
    #prom = numpy.concatenate ((x,y))
    #prom.shape = (4,10)
    #write_matrix_to_file(prom,name+'_prom.txt',presentado,traspose=True)

    #calculo el vector complejo que guarda theta y el radio

    complejo = numpy.array([])
    theta =[]
    radio_2 = pow(prom_cos,2)+pow(prom_sin,2)
    for i in range (10):
        if prom_cos[i] < 0:
            theta1= numpy.arctan(prom_sin[i]/prom_cos[i])+math.pi
        else:
            if prom_sin [i] > 0:
                theta1= numpy.arctan(prom_sin[i]/prom_cos[i])
            else:
                theta1= numpy.arctan(prom_sin[i]/prom_cos[i])+2*math.pi
        theta.append(theta1)
    complejo = numpy.concatenate((radio_2,theta))
    complejo.shape = (2,10)
    #write_matrix_to_file(complejo,name+'_complejo.txt',presentado,traspose=True)

    e_complejo = numpy.array([])
    e_theta = []
    e_radio_2 = pow(prom_e_cos,2)+pow(prom_e_sin,2)
    for i in range(10):
        if prom_e_cos[i] < 0:
            thetae= numpy.arctan(prom_e_sin[i]/prom_e_cos[i])+math.pi
        else:
            if prom_e_sin [i] > 0:
                thetae= numpy.arctan(prom_e_sin[i]/prom_e_cos[i])
            else:
                thetae= numpy.arctan(prom_e_sin[i]/prom_e_cos[i])+2*math.pi
        e_theta.append(thetae)
    e_theta= numpy.arctan2(prom_e_sin,prom_e_cos)
    e_complejo = numpy.concatenate((e_radio_2,e_theta))
    e_complejo.shape = (2,10)
    #write_matrix_to_file(e_complejo,name+'_e_complejo.txt',presentado,traspose=True)

    #mapeo los promedios a sen y cos de un angulo
    
    fx = map (math.cos,theta)
    fy = map (math.sin,theta)
    e_fx = map (math.cos,e_theta)
    e_fy = map (math.sin,e_theta)

    #calculo la correlacion
    
    corr = numpy.array([])
    for j in range (10):  
        corr = numpy.concatenate((corr,(sin[:,j] - prom_sin[j])*(cos[:,j] - prom_cos[j])))
    corr.shape = (-1,10)
    prom_corr = numpy.mean(corr,axis=0)/(cant-1)
    mat_corr = numpy.concatenate((varianza_cos,varianza_sin,prom_corr))
    mat_corr.shape = (3,10)
    #write_matrix_to_file(mat_corr,name+'_correlation.txt',presentado,traspose=True)

    e_corr = numpy.array([])
    for j in range (10):  
        e_corr = numpy.concatenate((e_corr,(e_sin[:,j] - prom_e_sin[j])*(e_cos[:,j] - prom_e_cos[j])))
    e_corr.shape = (-1,10)
    prom_e_corr = numpy.mean(e_corr,axis=0)/(cant-1)
    mat_e_corr = numpy.concatenate((varianza_e_cos,varianza_e_sin,prom_e_corr))
    mat_e_corr.shape = (3,10)
    #write_matrix_to_file(mat_e_corr,name+'_e_correlation.txt',presentado,traspose=True)

    #calculo el error teniendo en cuenta la correlación
    
    error_theta_2 = numpy.array([])
    error_theta_2 =(-fy * (-varianza_cos * fy + prom_corr * fx)+ fx* (-prom_corr * fy + varianza_sin * fx))/radio_2
    error_theta = map(math.sqrt,error_theta_2)
    error_theta.shape = (1,10)
    #write_matrix_to_file(error_theta,name+'_error_theta_2.txt',presentado,traspose=True)
    dato = numpy.vstack((theta,error_theta,radio_2))
    dato.shape = (3,10)
    write_matrix_to_file(dato,name+'_dato.txt',presentado,traspose=True)

    e_error_theta_2 = numpy.array([])
    e_error_theta_2 =(-e_fy * (-varianza_e_cos * e_fy + prom_e_corr * e_fx)+ e_fx* (-prom_e_corr * e_fy + varianza_e_sin * e_fx))/e_radio_2
    e_error_theta_2.shape = (1,10)
    inconsistencia = numpy.mean(e_error_theta_2)
    print(inconsistencia)
    e_error_theta = map(math.sqrt,error_theta_2)
    print(e_theta)
    print(e_error_theta)
    e_error_theta.shape = (1,10)
    #write_matrix_to_file(e_error_theta,name+'_e_error_theta_2.txt',presentado,traspose=True)
    e_dato = numpy.vstack((e_theta,e_error_theta,e_radio_2))
    e_dato.shape = (3,10)
    write_matrix_to_file(e_dato,name+'_e_dato.txt',presentado,traspose=True)


    #calculo la variabilidad estratégica 1 y 2.
    
    var1 = pow(e_error_theta-math.sqrt(inconsistencia),2)
    variabilidad_1 = numpy.mean(var1)/inconsistencia
    print(variabilidad_1)

    var2= pow(e_theta/e_error_theta,2)
    variabilidad_2=numpy.mean (var2)
    print (variabilidad_2)

    var_rodri = pow((e_theta-prom_errores)/error_theta,2)
    print (var_rodri)
    variabilidad_rodri = numpy.mean(var_rodri)*10
    print (variabilidad_rodri)
    
    globales = numpy.array([])
    globales = [prom_errores,prom_puntaje,inconsistencia,variabilidad_1,variabilidad_2,variabilidad_rodri,pereza]
    #print (globales)
    file.write(name)
    file.write ("\t")
    file.write(str(edad))
    file.write ("\t")
    file.write(sexo)
    file.write ("\t")
    file.write(juego)
    file.write ("\t")
    file.write(str(cant))
    file.write("\t")
    for elemento in globales:
        file.write(str(elemento))
        file.write("\t")
    file.write("\n")

    file.close()
    
    print('Se ve que todo anduvo, TE AMO MI VIDA !')
if __name__ == '__main__':
    Main() #ejecuto el Main
