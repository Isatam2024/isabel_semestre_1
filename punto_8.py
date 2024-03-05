#promoción fin de año de motocicletas.
#Descuento Motos marca Honda 5%
#Descuento Motos marca Yamaha 8%
#Descuento Motos marca Suzuki 10%
#Descuento otras marcas 2%
#Mostrar: precio de la moto,descuento y precio a pagar.
Precio_moto = int(input("Ingrese el precio de la moto:"))
Marca = (input("Ingrese la marca de la moto: "))
if Marca == "Honda":
    Descuento = 0.05
    Precio_pagar = Precio_moto - Descuento
    print(f"¡Tiene un descuento del 5%!,el precio a pagar de la moto es de {Precio_pagar}")
elif Marca == "Yamaha":
    Descuento = 0.08
    Precio_pagar = Precio_moto - Descuento
    print(f"¡Tiene un descuento del 8%!,el precio a pagar de la moto es de {Precio_pagar}")
elif Marca == "Suzuki" :
    Descuento = 0.10
    Precio_pagar = Precio_moto - Descuento
    print(f"¡Tiene un descuento del 10%!,el precio a pagar de la moto es de {Precio_pagar}")
else :
    Descuento = 0.02
    Precio_pagar = Precio_moto - Descuento
    print(f"¡Tiene un descuento del 2%!,el precio a pagar de la mota es de {Precio_pagar}")