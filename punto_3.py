#Ingresar por teclado 3 números enteros y mostrar el menor de los 3 números ingresados y la suma de dichos números.
#Ingreso de  tres números
num1 = float(input("Ingrese el num1:"))
num2 = float(input("Ingrese el num2:"))
num3 = float (input("Ingrese el num3:"))
#menor de los números
if num1 < num2 and num1 < num3:
    print (f"el menor de los tres números es el {num1}")
elif num2 < num1 and num2 < num3:
    print (f"el menor de los tres números es el {num2}")
elif num3 < num1 and num3 < num2:
    print (f"el menor de los tres números es el {num3}")
else:
    print("Error,los número ingresados son similares.")
#suma
Suma = num1 + num2 + num3
print(f"el resultado de la suma de los tres números es {Suma}")


