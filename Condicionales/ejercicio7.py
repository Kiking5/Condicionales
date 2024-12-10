"""Los tramos impositivos para la declaración de la renta en un determinado 
país son los siguientes:

Renta	                    Tipo impositivo
Menos de 10000€	            5%
Entre 10000€ y 20000€	    15%
Entre 20000€ y 35000€	    20%
Entre 35000€ y 60000€	    30%
Más de 60000€	            45%
Escribir un programa que pregunte al usuario su renta anual y muestre por 
pantalla el tipo impositivo que le corresponde."""

renta = int(input("Ingrese su Renta anual: "))
if renta >= 60000:
    print(f"Su renta es de {renta}, su Tipo de impositivo es del 45%, usted debe pagar {(renta*45)/100}")
elif renta >= 35000:
    print(f"Su renta es de {renta}, su Tipo de impositivo es del 30%. usted debe pagar {(renta*30)/100}")
elif renta >= 20000:
    print(f"Su renta es de {renta}, su Tipo de impositivo es del 20%. usted debe pagar {(renta*20)/100}")
elif renta >= 10000:
    print(f"Su renta es de {renta}, su Tipo de impositivo es del 15%.usted debe pagar {(renta*15)/100}")
else:
    print(f"Su renta es de {renta}, su Tipo de impositivo es del 5%. usted debe pagar {(renta*5)/100}")