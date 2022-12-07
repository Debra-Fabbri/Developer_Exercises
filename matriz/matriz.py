"""
## Ejercicio Matriz

Se solicita crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.

"""

import numpy as np

#m = np.random.randint(1,100, size=(5,5))
#print(m)


# Creamos una funcion que nos permitira crear una matriz de 5x5 randomizada con números enteros, 
# y encontrar secuencia de 4 consecutivos horizontal o vertical 

def EjercicioMatriz(M, num_consecutivo=4):

    for v in np.vstack((M, M.T)): # Debe comprobar tanto las columnas como las filas
        count = 1         # Registrar cuántos números consecutivos se han encontrado
        current_num = 0   # Registrar 1 o -1
        for i in range(1, len(v)):
            diff = v[i] - v[i-1]

            if diff == 1:  # si la diferencia es 1
                if current_num != 1: # si la diferencia anterior no es 1, reiniciar el contador
                    count = 1
                current_num = 1
                count += 1
            elif diff == -1:
                if current_num != -1: count = 1
                current_num = -1
                count += 1
            else: # reiniciar contador
                current_num = 0
                count = 1
            if count == num_consecutivo:
                return True
    return False


M = np.random.randint(1,100, size=(5,5))

print(M, EjercicioMatriz(M, 4))

print(" ")
print(" ")


#Test para ver si se encuentra: horizontal
M2 = np.array([  [10, 43, 74, 32, 69],
                [20, 19, 69, 83,  8],
                [89, 31, 62, 61, 17],
                [35,  3, 77, 22, 29],
                [52, 53, 54, 55, 73] ])

print(M2, EjercicioMatriz(M2, 4))

print(" ")
print(" ")


#Test para ver si se encuentra: vertical
M3 = np.array([  [10, 43, 74, 32, 69],
                [20, 19, 69, 33,  8],
                [89, 31, 62, 34, 17],
                [35,  3, 77, 35, 29],
                [52, 53, 54, 5, 73] ])

print(M3, EjercicioMatriz(M3, 4))

