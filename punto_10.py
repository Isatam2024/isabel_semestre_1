#Un cliente va a comprar una moto y se percata que si lo compraba el martes tiene un descuento del 12%, luego
# si lo compra el sábado tiene un descuento del 18% y si es feriado un 25%, mostrar cuanto pagara en cada opción.
CM = float(input("Ingresar el costo de la moto:")) #CM=costo de la moto
DC = input ("Ingresar el dia de compra de la moto:")
#Pago con descuento
if DC == "Martes":
        print("El costo con el 12% de descuento es: ", CM * 0.12)
elif DC == "Sábado":
        print("El costo con el 18% de descuento es: ", CM * 0.18)
elif DC == "Feriado" :
        print("El costo con el 25% de descuento es: ", CM * 0.25)
else :
    print("El costo sin descuento es: ", CM)