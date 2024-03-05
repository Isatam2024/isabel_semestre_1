#A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora.
TH = 5532
# si la cantidad de horas trabajadas es mayor a 40 horas la tarifa se incrementa en un 50% para las horas extras.
CHT = float(input("Ingresar la cantidad de horas trabajadas:"))
# calcular el salario del trabajador dadas las horas trabajadas y la tarifa.
SSH = TH * CHT
SCH = SSH + ((CHT-40) * (0.5*TH))
if CHT > 40 :
    print (f"Tiene horas extra,su salaraio es {SCH}")
else :
    print (f"No tiene  horas extras su salario es {SSH}")