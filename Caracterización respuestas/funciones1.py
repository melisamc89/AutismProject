import math
import numpy
import os

def xatheta(v):
    return (2*math.pi*((v - 412)/ (857 - 412)))

def erroratheta(v):
    return (2*math.pi*(v/ (857 - 412)))

def ang(x):
    return ((x*360)/(2*math.pi))

def function_to_matrix(function, matrix):
    return [[function(elemento) for elemento in col] for col in matrix]

def write_list_to_file(lista, file):
    
    row = " ".join(str(elem) for elem in lista)
    print(row, file=file)

def write_matrix_to_file(matrix, file_name, pre_row=None, traspose=False):

    with open(file_name, 'w') as output: #abro archivo (cierre automatico)
        
        if pre_row is not None:
            pre_row.shape = (1, 10)
            matrix = numpy.concatenate((pre_row, matrix))
        
        if traspose:
            matrix = numpy.transpose(matrix)
        
        for row in matrix:
            write_list_to_file(row, output)
            
def dividir(elemento,cant):
    return float(elemento/cant)

def arctan3(y,x):

    if x < 0:
        return numpy.arctan(y/x)+math.pi
    else:
        if y > 0:
            return numpy.arctan(y/x)
        else:
            return numpy.arctan(y/x)+2*math.pi

def fpereza (name,cant):
    
    sums = numpy.array([])
    error = numpy.array([])

    direc = os.path.join('.','datos',name+str(1)+'.txt')
    presentado = numpy.loadtxt(direc,skiprows=1,usecols=(0,),dtype=int,unpack=True)

    for i in range(cant):
        path = os.path.join('.','datos', name + str(i + 1) + '.txt') 
        col1,col2 = numpy.loadtxt(path,skiprows=1,usecols=(0,1),dtype=int,unpack=True)
        suma_col = col1+col2
        sums = numpy.concatenate((sums,suma_col))
        error = numpy.concatenate((error, col2))    

    sums.shape = (-1,10)
    error.shape = (-1,10)
    
    #prom_respuesta= numpy.mean(sums,axis=0)
    prom_error= numpy.mean(error,axis=0)

    recta = numpy.polyfit (presentado,prom_error,1)
    pereza = recta[0]
    ordenada = recta[1]
    
    return recta

def analisis(name,cant,edad,sexo,juego):

    pereza,b = fpereza (name,cant)
    
    sums = numpy.array([])
    error = numpy.array([])

    for i in range(cant):
        path = os.path.join('.','datos',name + str(i + 1) + '.txt') 
        col1,col2 = numpy.loadtxt(path,skiprows=1,usecols=(0,1),dtype=int,unpack=True)
        suma_col = col1+col2 #-(pereza*col1)-b
        error_col = col2 #-(pereza*col1)-b
        sums = numpy.concatenate((sums,suma_col))
        error = numpy.concatenate((error, error_col))

    file = open(os.path.join('.','sin pereza.txt'),'a')

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
    #write_matrix_to_file(error,name+'_error.txt',col1,traspose=True)
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
    varian_sin = numpy.var(sin,axis=0)*cant/(cant-1)
    varianza_sin = map(math.sqrt,varian_sin)
    y = numpy.concatenate ((prom_sin,varianza_sin))
    y.shape = (2,10)
    #write_matrix_to_file(y,name+'_prom_sin.txt',presentado,traspose=True)
    e_y = numpy.array([])
    prom_e_sin = numpy.mean(e_sin,axis=0)
    varian_e_sin = numpy.var(e_sin,axis=0)*cant/(cant-1)
    varianza_e_sin = map(math.sqrt,varian_e_sin)
    e_y = numpy.concatenate ((prom_e_sin,varianza_e_sin))
    e_y.shape = (2,10)
    #write_matrix_to_file(e_y,name+'_prom_sin.txt',presentado,traspose=True)

    x = numpy.array([])
    prom_cos = numpy.mean(cos,axis=0)
    varian_cos = numpy.var(cos,axis=0)*cant/(cant-1)
    varianza_cos = map(math.sqrt, varian_cos )
    x = numpy.concatenate ((prom_cos,varianza_cos))
    x.shape = (2,10)
    #write_matrix_to_file(x,name+'_prom_e_cos.txt',presentado,traspose=True)
    e_x = numpy.array([])
    prom_e_cos = numpy.mean(e_cos,axis=0)
    varian_e_cos = numpy.var(e_cos,axis=0)*cant/(cant-1)
    varianza_e_cos = map(math.sqrt, varian_e_cos )
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
    
    error_theta_2 = numpy.array([])
    error_theta_2 = 1 - map(math.sqrt,radio_2)
    error_theta = map(math.sqrt,error_theta_2)
    #error_theta.shape = (1,10)

    dato = numpy.array([])
    dato = numpy.concatenate ((theta,error_theta))
    dato.shape = (-1,10)
    #write_matrix_to_file(dato,name+'_dato_sin_pereza.txt',presentado,traspose=True)

    e_error_theta_2 = numpy.array([])
    e_error_theta_2 = 1 - map(math.sqrt,e_radio_2)
    inconsistencia = numpy.mean(e_error_theta_2)
    print(inconsistencia)
    e_error_theta = map(math.sqrt,error_theta_2)
    #e_error_theta.shape = (1,10)
    
    e_dato = numpy.array([])
    e_dato = numpy.concatenate ((e_theta, e_error_theta))
    e_dato.shape = (-1,10)
    #write_matrix_to_file(e_dato,name+'_e_dato_sin_pereza.txt',presentado,traspose=True)


    #calculo la variabilidad estratégica 1, 2 y rodri
    
    var1 = pow(e_error_theta-math.sqrt(inconsistencia),2)
    variabilidad_1 = numpy.mean(var1)/inconsistencia
    print(variabilidad_1)
    
    var2= pow(e_theta/e_error_theta,2)
    variabilidad_2=numpy.mean (var2)
    print (variabilidad_2)

    var_rodri = pow(((e_theta - prom_errores)/error_theta),2)
    variabilidad_rodri = numpy.mean(var_rodri)*10
    print (variabilidad_rodri)
    print(pereza)
    
    globales = numpy.array([])
    globales = [prom_errores,prom_puntaje,inconsistencia,pereza]
    #globales = [variabilidad_1,variabilidad_2,variabilidad_rodri]
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
    
