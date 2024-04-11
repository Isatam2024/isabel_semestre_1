#7.	Desarrolle un programa que calcule el promedio de edad hombre y mujeres de un grupo de estudiantes.
lista_h = [4, 5, 6, 7]
lista_m = [8, 9, 10, 11]
suma = 0
suma_m = 0
contador = 0
p=len(lista_h)
p_2=len(lista_m)
while contador<len(lista_h):
     suma += lista_h[contador]
     suma_m += lista_m[contador]
     contador += 1
print(f"el promedio de los hombres es :{suma/p}")
print(f"el promedio de los mujeres es :{suma_m/p_2}")

