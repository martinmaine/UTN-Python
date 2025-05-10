print ("Hola Mundo")

ingreso = int(input("Ingrese edad: ")) #se aclara el tipo de dato antes del input
print ("tu edad duplicada es", ingreso * 2) 
print("Podemos separa tu edad con sep, tu edad es:",ingreso, sep=" ") #podemos ingrar por ejemplo sep="**" y lo separará con **. En el ejemplo se separa con espacio. La coma también coloca por defecto un espacio.
concatenar = "Tu edad concatenada es " + str(ingreso) + " años"
print (concatenar)
print (f"Tu edad concatenada es {ingreso} años")
print("Descartes dijo: \"Pienso, luego existo\" ") #\ con alt 92 usamos un caracter de escape.

print("uno\nDos\nTres")  #\t hace saltos de tabulación, \n hace salto de linea

