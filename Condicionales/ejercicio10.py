"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus 
clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
y en función de su respuesta le muestre un menú con los ingredientes disponibles 
para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el 
tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la 
pizza elegida es vegetariana o no y todos los ingredientes que lleva."""


tipo = int(input(f"Elija un tipo de Pizza, \n1: Vegetariana \n2: No vegetariana \n"))

if tipo == 1:
    ingrediente = int(input(f"Elija el ingrediente vegetariano: \n1: Pimiento \n2: Tofu \n"))
    if ingrediente == 1:
        print(f"Usted selecciono su Pizza vegetariana con mozzarella, tomate y pimiento")
    else:
        print(f"Usted selecciono su Pizza vegetariana con mozzarella, tomate y tofu")

else:
    ingrediente = int(input(f"Elija el ingrediente No vegetariano: \n1: Peperoni \n2: Jamón \n3: Salmón \n"))
    if ingrediente == 1:
        print(f"Usted selecciono su Pizza no vegetariana con mozzarella, tomate y peperoni")
    elif ingrediente == 2:
        print(f"Usted selecciono su Pizza no vegetariana con mozzarella, tomate y jamón")
    else:
        print(f"Usted selecciono su Pizza no vegetariana con mozzarella, tomate y salmón")