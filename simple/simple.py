"""
## Ejercicio Simple

Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
elementos. retornar la lista.

"""

import random

def EjercicioSimple(n):
    dicccionario = {} # se inicializa un dic vacio

    p = [] #lista vacia
    p.append(dicccionario) # se agrega el diccionario a la lista

    for i in range(1, n + 1): # se crean los id
        dicccionario[i] = [] # se agregan al diccionario como claves
        
        for c in dicccionario: 
            c = random.randint(1,100) # se crean las edades aleatoreas
            dicccionario[i] = c # se agregan al diccionario como valores

    #return type(p) # Para correr el test debe de borrar el comentado 
    return p # se retorna la lista de diccionarios


res = EjercicioSimple(10) # paso parametro 10 como longitud
print(res)
