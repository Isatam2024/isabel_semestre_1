#Definición de algoritmo para lea cuatro notas (de 1 a 5) para promedio :
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))
nota_promedio = (nota1 + nota2 + nota3 + nota4) / 4
#Rendimiento de acuerdo a promedio
if 4 < nota_promedio <= 5:
    print("Rendimiento: Excelente")
elif 3 < nota_promedio <= 4:
    print("Rendimiento: Bien")
else:
    print("Rendimiento: Deficiente")
#Aplicaciónd de descuento en matricula para aquellos estudiantes que obtienen un rendimiento excelente
if 4 < nota_promedio <= 5:
    print("Tiene un descuento del 20% en la matricula")
else:
    print("Paga el 100% de la matricula: ")


