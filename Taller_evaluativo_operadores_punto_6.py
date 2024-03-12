#6.	El gobierno nacional ha decretado un incremento del 4,2% para el salario mínimo del próximo año.
# Elabore un algoritmo que muestre el nuevo salario mínimo para el siguiente año.
Salario_año_pasado = float(input("Ingrese el salario del año pasado:"))
Salario_año_actual = Salario_año_pasado + (0.042*Salario_año_pasado)
print(f"El nuevo salario mínimo para el año siguiente es: {Salario_año_actual}")
