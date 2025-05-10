""" print (4 < 5)
print (4 > 5)
print ( 4 <= 5 )
print (5 >= 5 )
print ( 4 == 5 )
print ( 4 != 5 )


EDAD_MINIMA = 18
edad = int(input("ingrese su edad: "))
categorias = input("ingrese su categoría (A, B, C, D, E)")

if edad >= EDAD_MINIMA and (categorias == "D" or categorias == "d"): 
    print ("PUEDE CONDUCIR AMBULANCIA") 
else:
    print ("NO PUEDE CONDUCIR AMBULANCIA") """

import random

numero_correcto = random.randint(1, 100) 

numero_usuario = int(input("Adivina el número entre 1 y 100: ")) 


if numero_usuario ==  numero_correcto: 
    print("¡Has adivinado el número!") 
elif numero_usuario <= numero_correcto:
    print("Intenta con un número mayor.") 
else:
    print("Intenta con un número menor.")