#A un trabajador le descuentan de su sueldo el 10%, si su sueldo es menor o igual a 1000.
Sueldo = float(input("Ingrese el sueldo del trabajador:"))
TD1 = Sueldo - (Sueldo*0.10)
TD2 = Sueldo - (Sueldo*0.05)
TD3 = Sueldo - (Sueldo*0.03)
if Sueldo <= 1000 :
    print (f"su sueldo neto es {TD1}")
elif  Sueldo >1000 and Sueldo <= 2000 :
    print(f"su sueldo neto es {TD2}")
else :
    print (f"su sueldo neto es {TD3}")
