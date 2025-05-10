""" TP 1 Secuenciales: """
""" 1)  """
print("Hola Mundo!")
""" 2) """
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

""" 3)  """
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

""" 4)  """
import math
radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

""" 5) """
segundos = int(input("Ingresa una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas")

""" 6) """
numero = int(input("Ingresa un número:"))

print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")

""" 7)  """
num1 = float(input("Ingresa el primer número (distinto de 0): "))
num2 = float(input("Ingresa el segundo número (distinto de 0): "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")

""" 8) """
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

""" 9) """
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit")

""" 10) """
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")


