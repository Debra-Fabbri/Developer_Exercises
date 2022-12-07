"""
## Ejercicio Clases

Se solicita escribir una clase en python llamada círculo que contenga un radio, con un método que
devuelva el área y otro que devuelva el perímetro del círculo.

>> Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
usuario e impidiendo la instanciación. ✔ 
>> Si printeamos el objeto creado debe mostrarse una representación amigable. ✔ 
>> El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
mostrar un error y no permitir modificación. ✔ 
>> Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
multiplicado por n. No permitir la multiplicación por números <= 0
"""

# Para la resolución de este ejercicio, desde la librería math importaremos la función "pi" que nos
# permitirá trabajar y obtener un valor/respuesta mas específica

from math import pi

# Primeramente se creará una función que servirá para correr los tests
# los mismo estan seteados en el archivo "tests.py"
# para poder modificar e ingresar manualmente el radio debe borrar en la linea 54 el # 
# y el programa prodra ejecutarse 



# se crea la clase circulo y definimos los métodos necesarios

def EjercicioClases(radio, n):

        class NoCero(Exception):
            def __init__(self):
                pass
            # no necesito nada de esta clase ahora, salvo invocarla


        class circulo():
            # primero se crea un constructor indicando que es un método de instancia: "self" y luego el parámetro "radio"
            def __init__(self, radio):
                self.radio = radio

            #luego los métodos de instancia:
            def area(self):
                return (pi * self.radio ** 2)

            def perimetro(self):
                return (2 * pi * self.radio)

            def __repr__(self):
                return "Este es el objeto de la clase circulo"
        

        try:
            #radio = int(input("Ingrese el radio: "))
            if radio <= 0:
                raise NoCero()
                # acá se verfica el valor a pasar y el llamado a la clase de "valor no cero"
            print(f"El radio es: {radio}")
            
            # Si ambos valores son enteros y mayores que cero instancio a la clase circulo
            c = circulo(radio)
            area = c.area()
            perimetro = c.perimetro()

            resultado_test = [area, perimetro]

            print(f"El area del circulo es: ", area)
            print(f"El perimetro del circulo es: ", perimetro)

            clase = circulo(radio)
            print(clase)

            return resultado_test
        
        except NoCero as e:
            print("UPS!! :/ El número ingresado no puede ser 0 o un valor negativo")
            # el error por la clase

        return