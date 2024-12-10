"""Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo 
y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la 
M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir 
un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el 
grupo que le corresponde."""

nombre = input("Ingrese su nombre: ").capitalize()
sexo = input("Ingrese su sexo (M para mujer, H para hombre): ").upper()

if sexo == "M" and nombre < "M": # Sexo es igual a Mujer y nombre es anterior a M
    grupo = "A"
elif sexo == "H" and nombre > "N": # Sexo es Hombre y nombre es posterios a N
    grupo = "A"
else:
    grupo = "B"  # de lo contrario es B

print(f"Pertenece al grupo {grupo}.")