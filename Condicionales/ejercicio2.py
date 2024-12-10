"""Escribir un programa que almacene la cadena de caracteres contraseña en una 
variable, pregunte al usuario por la contraseña e imprima por pantalla si la 
contraseña introducida por el usuario coincide con la guardada en la variable 
sin tener en cuenta mayúsculas y minúsculas."""

contrasena = ("qwertyuiop")

usuario_contrasena = input("Ingrese su contraseña: ")
if contrasena == usuario_contrasena:
    print("Contraseña válida.")
elif usuario_contrasena.lower() == contrasena:
    print("La contraseña es válida. ")
else:
    print("La contraseña es incorrecta. ")

