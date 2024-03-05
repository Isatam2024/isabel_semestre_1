#.Desarrolle un algoritmo que permita leer tres valores y almacenarlos   en   las variables num1, num2, num3 respectivamente. El algoritmo debe imprimir cual es el mayor. Recuerde constatar que los tres valores introducidos por el teclado sean valores distintos.
#Asignar tres valores
num1 = float(input("Ingrese el num1:"))
num2 = float(input("Ingrese el num2:"))
num3 = float (input("Ingrese el num3:"))
#mostrar mayor de tres valores
if num1 > num2 and num1 > num3:
    print (f"el mayor de los tres números es el {num1}")
if num2 > num1 and num2 > num3:
    print(f"el mayor de los tres números es el {num2}")
if num3 > num1 and num3 > num2:
    print(f"el mayor de los números es el{num3}")
else:
    print("Error,los número ingresados son similares.")