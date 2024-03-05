#7.Determinar si un alumno aprueba o reprueba un curso,
# sabiendo que aprobara si su promedio de cinco calificaciones es mayor o igual a 5;
#reprueba en caso contrario.
#Introducimos las notas el alumno
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))
nota5 = float(input("Ingrese la nota 5: "))
nota_promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5 #con esta ecuación sacamos la nota promedio
#Vamos a crear un codigo que permita saber si el alumno aprueba o reprueba
if nota_promedio >= 5:
    print(f"Su nota es {nota_promedio},ha aprobado el curso.")
else:
    print(f"Su nota es {nota_promedio},ha reprobado el curso.")



