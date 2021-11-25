# Xavier Calvo
# Octubre 2021
# FISABIO 
# Programa para la automatización en la creación de líneas de código en formato (IL)
# Para el autómata de Schneider TM221

from itertools import product
import os

# Contador numero de linea
cnt = 0

# Registros por dia
reg_dia = 12

# Variables seleccion usuario
dias = 7
registro = 0

salida = "SALIDA"

# lista para preparar datos de escritura
escritura = []
resultado = ''

def preparaEscritura(d):     
    escritura.append(str(registro-1) + ':X' + str(d-1))    
    escritura.append(d)

    for i in range(0,12):
        escritura.append(str(registro + ((d- 1) * reg_dia) + i))
    
    escritura.append(str(d-1))
    #print(escritura)

# Ejecución programa
print('Seleccionar los datos para la generación del programa para el automata TM221 \n') 
print('\nIntroduce el registro inicial: (Por ejemplo 300) \n')
registro = int(input()) + 1

for day in range(1, dias+1):
    preparaEscritura(day)

    # Generación Fichero salida para los bloques
    with open('./plantillas/plantilla.txt','r') as plantilla:
            
        lineas = plantilla.readlines()
        contador = 0

        for line in lineas:  
                    
            if not line.startswith(')'):
                resultado += line.format(escritura[cnt]) 
                cnt += 1
            else:
                resultado += ')\n'

    # Escritura fichero de salida para los bloques
    with open('programa_' + 'dia_' + str(day) + '_reg_' + str(registro-1) + '.txt', 'w') as writer:
        writer.write(resultado)
        resultado = ""

    
print('\n Se ha creado el programa correctamente', '\n \n')
#print(resultado)


 

