#Hacer un algoritmo que calcule el total a pagar por la compra de camisas.
NCC = float(input("ingrese número de camisas compradas:"))
TU = 20000
#Si se compran tres camisas o más se aplica un descuento del 20% sobre el total de la compra y si son menos de tres camisas un descuento del 10%
TD1 = (NCC * TU) - ((NCC * TU) * 0.10)
TD2 = (NCC * TU) - ((NCC * TU) * 0.20)
if NCC <3 :
    print (f"El valor de las camisas es: {TD1}")
else :
    print (f"El valor de las camisas es {TD2}")