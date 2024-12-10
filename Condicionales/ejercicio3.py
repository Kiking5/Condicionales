"""Escribir un programa que pida al usuario dos números y muestre por pantalla 
su división. Si el divisor es cero el programa debe mostrar un error."""

numero1 = int(input("Ingrese un numero (Dividendo): "))
numero2 = int(input("Ingrese un numero (divisor): "))

if numero2 == 0:
    print("Error en la división!")
else:
    print(f"{numero1}, dividido entre {numero2} es igual a: {(numero1/numero2)}")