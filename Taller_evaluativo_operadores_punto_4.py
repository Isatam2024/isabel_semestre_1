#4. 4.	En un curso de “fundamentos de algoritmos”,
# se tienen las siguientes notas (Cada una de ellas entre 1 y 5) con sus respectivos porcentajes:
#Taller 1: 20%
#Taller 2: 15%
#Cuestionario 1:22%
#Cuestionario 2:10%
#Proyecto final: 33%
#Escribir un algoritmo que lea las cinco notas de un estudiante e imprima la nota definitiva.
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))
nota5 = float(input("Ingrese la nota 5: "))
nota_promedio = ((0.20*nota1) + (0.15*nota2) + (0.22*nota3) + (0.10*nota4)+ (0.33*nota5))
print (f"Su nota final del curso de programación es {nota_promedio}")