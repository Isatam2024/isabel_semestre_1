#2.	Una empresa de llamadas al exterior tiene las siguientes tarifas por minuto (TPM):
TPM_EEUU = 900
TPM_CAD = 800
TPM_EU = 950
TPM_RESTO_DEL_MUNDO = 1250
porcentaje_descuento= 0.2 #Si la duración de la llamada es superior a 15 minutos, se aplica un descuento del 20% al valor de la llamada.
duración = int(input("Ingrese la duración de la llamada:"))
región =(input("Ingrese la región de la llamada EEUU,CAD, EU or RESTO_DEL_MUNDO:"))
#costo sin descuento
if región == "EEUU":
   costo_sin_descuento= TPM_EEUU * duración
elif región == "CAD":
    costo_sin_descuento= TPM_CAD * duración
elif región == "EU":
    costo_sin_descuento= TPM_EU * duración
else:
    costo_sin_descuento= TPM_RESTO_DEL_MUNDO * duración
#costo con descuento
if duración > 15:
    descuento= costo_sin_descuento * porcentaje_descuento
    costo_con_descuento= costo_sin_descuento - descuento
    print("El costo con el 20% de descuento es: ", costo_con_descuento)
else:
    print("El costo sin el 20% de descuento es: ", costo_sin_descuento)
