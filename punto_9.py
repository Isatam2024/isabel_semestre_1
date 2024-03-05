#Pedir un valor numérico e indicar si es par o no es par.
print ("Evaluador de números pares o impares")
numero = int(input("Ingrese número a evaluar: "))
if numero % 2 == 0:
    print("El número es par")
else :
    print("El número es impar")